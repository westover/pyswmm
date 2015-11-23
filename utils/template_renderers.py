from __future__ import print_function, unicode_literals, division
import os
from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('pyswmm', os.path.abspath('../templates')))
from datetime import date, timedelta

SIMPLE_TEMPLATE = {
    'FLOW_UNITS': 'CFS',
    'START_DATE': date(2013, 5, 10),
    'END_DATE': date(2013, 6, 24),
    'WET_STEP': timedelta(minutes=30),
    'DRY_STEP': timedelta(minutes=60),
    'ROUTING_STEP': timedelta(seconds=30),
    'SUBCATCHMENTS': [],
    'RAIN GAUGES': []
}


def simple_template_render(**kwargs):
    """
    Take in any keyword args and render the simple swmm template
    :param kwargs:
    :return:
    """
    options = SIMPLE_TEMPLATE.update(kwargs)
    template_file = 'swmm_simple.inp.j2'
    rendered_file = render_template(template_file, options)
    return rendered_file


def render_template(template_file, options):
    """
    Given a template path and options render the template with those options specified
    :param template_file:
    :param options:
    :return:
    """

    return env.get_template(template_file).render(**options)