"""Collection of utilities to do some input file manipulation and output file scraping"""
from __future__ import print_function, unicode_literals, division
from .output_parser import RPTOutputReader
from .input_manipulator import InputManipulator


# For convenience the class methods are defined into static functions

# Input file manipulation

# Modify the impervious cover for any subcatchment
modify_impervious_cover = InputManipulator().modify_impervious_cover

# Collect of tools for getting and setting LID features
get_LID_controls = InputManipulator().get_LID_controls
get_LID_usage = InputManipulator().get_LID_usage
set_LID_usage = InputManipulator().set_LID_usage

# Output file manipulation
extract_subcatchment_summary_data = RPTOutputReader().extract_subcatchment_summary_data


def calculate_area_from_polygon(polygon):
    pass


def find_longest_segment_of_polygon(polygon):
    pass

