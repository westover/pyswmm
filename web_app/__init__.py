from flask import Flask, redirect, url_for
from flask import request
from flask.ext.restful import Resource, Api, reqparse
from flask.ext.cors import CORS
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
from utils import RPTOutputReader
from pyswmm.swmm5 import pyswmm
import traceback
import threading
import random


app = Flask(__name__)
CORS(app, resources=r'/rest/*', headers='Content-Type')
api = Api(app)

LOCAL = False

RESULTS = {}

MAX_SIMULATIONS = 2

SIMULATION_LOCK = threading.Semaphore(MAX_SIMULATIONS)


class SWMM(Resource):

    def get(self):
        global RESULTS
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('simid', help = 'simulation id')
            parser.add_argument('api_status', help = 'simulation id')
            d = parser.parse_args()
            print d
            # Code for checking the status of the api
            if d['api_status'] is not None:
                results = {
                    'active_simulation_count': threading.active_count(),
                    'result_count': len(RESULTS)
                    }
                return results

            if d['simid'] in RESULTS:
                return RESULTS[d['simid']]
            elif d['simid'] is not None:
                for this_thread in threading.enumerate():

                    if d['simid'] in this_thread.name:
                        try:
                            return {'status': this_thread.status}
                        except:
                            return {'status': 'waiting'}
                else:
                    return {'status': 'pending'}
            else:
                return d
        except:
            traceback.print_exc()

    def post(self):
        try:
            input_file = request.files['files[]'].read()
            this_simulation = Simulation(input_file)
            this_simulation.start()
            return {'simid': this_simulation.name}
        except:
            return 'ERROR: ' + traceback.format_exc()


class Simulation(threading.Thread):
    def __init__(self, input_file):
        super(Simulation, self).__init__()
        self.input_file = input_file
        self.status = 'pending'
        self.name = str(random.randint(0, 10000000))

    def run(self):
        global SIMULATION_LOCK, RESULTS
        with SIMULATION_LOCK:
            self.status = 'running'
            try:
                results = self.run_simulation()
            except:
                traceback.print_exc()
                results = {'status': 'ERROR: ' + traceback.format_exc()}
        RESULTS[self.name] = results

    def run_simulation(self):

        rtp_file = 'tmp/'+str(self.name)+'.rtp'
        output_file = 'tmp/'+str(self.name)+'.out'
        input_file = 'tmp/'+str(self.name)+'.inp'
        ifile = open(input_file, 'w')
        ifile.write(self.input_file)
        ifile.close()
        swmmobject = pyswmm(input_file, rtp_file, output_file)
        swmmobject.swmmExec()
        with open(rtp_file) as fp:
            rtp_output = RPTOutputReader.extract_subcatchment_summary_data(fp)
            fp.seek(0)
            raw_rtp_output = fp.read()

        self.status = 'complete'
        return {'status': 'complete', 'results': rtp_output, 'raw_output': raw_rtp_output}

api.add_resource(SWMM, '/rest/swmm')

@app.route('/')
def index():
    return redirect(url_for('static', filename='index.html'))


if __name__ == '__main__':
    app.run(debug=True)
