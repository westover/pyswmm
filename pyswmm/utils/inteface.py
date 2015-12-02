"""
Place to store interface classes
"""

from __future__ import print_function, unicode_literals, division
from datetime import datetime, timedelta

# Ok we need to construct an input file for SWMM

DEFAULT_OPTIONS = {
    "FLOW_UNITS": "CFS",
    "INFILTRATION": "HORTON",
    "FLOW_ROUTING": "KINWAVE",
    "START_DATE": datetime(2013, 5, 10),
    "START_TIME": timedelta(hours=0, minutes=0, seconds=0),
    "REPORT_START_DATE": datetime(2013, 5, 10),
    "REPORT_START_TIME": timedelta(hours=0, minutes=0, seconds=0),
    "END_DATE": datetime(2013, 6, 24),
    "END_TIME": timedelta(hours=12, minutes=0, seconds=0),
    "SWEEP_START": "01/01",
    "SWEEP_END": "12/31",
    "DRY_DAYS": 0,
    "REPORT_STEP": timedelta(hours=0, minutes=0, seconds=30),
    "WET_STEP": timedelta(hours=0, minutes=5, seconds=0),
    "DRY_STEP": timedelta(hours=1, minutes=0, seconds=0),
    "ROUTING_STEP": timedelta(hours=0, minutes=0, seconds=30),
    "ALLOW_PONDING": "NO",
    "INERTIAL_DAMPING": "PARTIAL",
    "VARIABLE_STEP": 0,
    "LENGTHENING_STEP": 0,
    "MIN_SURFAREA": 0,
    "NORMAL_FLOW_LIMITED": "BOTH",
    "SKIP_STEADY_STATE": "NO",
    "FORCE_MAIN_EQUATION": "H",
    "LINK_OFFSETS": "DEPTH",
    "MIN_SLOPE": 0
}
