"""
Output parsing classes
"""
from __future__ import print_function, unicode_literals, division

class RPTOutputReader(object):
    """ Class to read the rtp file output from SWMM and extract the runoff summary information and return that as a JSON
    """

    @classmethod
    def extract_subcatchment_summary_data(cls, output_file):
        """
        :param output_file: String of RTP output file
        :return: JSON string of parsed Subcatchment Summary area
        """
        # Break the file up by lines and turn it into an iterator
        lines = iter(output_file.splitlines())
        # Variable to track when the top of the block is found based on its name
        block_found = False

        # Where to store the data we plan to dump
        output_data = []

        # These are the fields that are found in this block
        HEADERS = [
            'Subcatchment',
            'Total Precip In',
            'Total Runon In',
            'Total Evap In',
            'Total Infill In',
            'Total Runoff In',
            'Total Runoff 10^6 gal',
            'Peak Runoff CPS',
            'Runoff Coeff'
        ]

        # Parse the file
        while True:
            # Grab the next line
            try:
                this_line = lines.next()
            except:
                break
            # If we found the block header sweet!
            if 'Subcatchment Runoff Summary' in this_line:
                block_found = True
                # Seek ahead 8 lines in the file to get to the actual data
                for i in range(8):
                    this_line = lines.next()
            # Lets handle the block of meaty data goodness
            if block_found:
                # This is a is the key that we have found the next block
                if '******************' in this_line:
                    break
                # Break the line up over whitespace
                this_line_list = this_line.split()
                # If the line is just a return move on
                if len(this_line_list) == 0:
                    continue
                # Lets parse the list we have the 0th element is the subcatchment name the rest are floats
                this_line_list = [this_line_list[0]] + map(float, this_line_list[1:])
                output_data.append(dict(zip(HEADERS, this_line_list)))
        # When we are finished json dumps the result
        import json
        return json.dumps(output_data)