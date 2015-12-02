from __future__ import print_function, unicode_literals, division

from hashlib import sha1

from ..utils import calculate_area_of_polygon, find_longest_segment_of_polygon

class Subcatchment(object):

    ARGS = (
        'name',
        'rain_gage_id',
        'outlet',
        'area',
        'percent_impervious',
        'width',
        'percent_slope',
        'curb_length',
        'snow_pack')


    OPTIONAL_ARGS = ('polygon', )


    def __init__(self, **kwargs):
        # Set the name to the hash if it isn't specified
        if 'name' not in kwargs:
            kwargs['name'] = sha1(str(kwargs)).hexdigest()
        if 'area' not in kwargs and 'polygon' in kwargs:
            kwargs['area'] = calculate_area_of_polygon(kwargs['polygon'])
        if 'width' not in kwargs and 'polygon' in kwargs:
            kwargs['width'] = find_longest_segment_of_polygon(kwargs['polygon'])
        if 'percent_slope' not in kwargs:
            kwargs['percent_slope'] = 0

        if len(set(self.ARGS) && set(kwargs.keys())) < len(self.ARGS):
            raise Exception(
                'Please specify {}'.format(', '.join(self.REQUIRED_ARGS)))



    def serialize_subcatchment(self):
        values = [getattr(self, this_arg, '') for this_arg in self.ARGS]
        return '\t'.join(values)

    def serialize_polygon(self):
        pass