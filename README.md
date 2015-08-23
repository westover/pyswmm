# PySWMM

This version of the library has diverged from the source.

In this version we expect that you will have the GDAL packages installed. As we expect to also read input from File GeoDatabase files.

The main communication primitive is intended to be GeoJSON feature/collection objects. 

Subcatchments -> Feature with geom_type of Polygon

Nodes -> Feature with geom_type of point

Vertices -> Feature with geom_type of line string

Options -> In a properties node of the FeatureCollection object

The properties node will contain either input conditions or output conditions.

We are heading in the path of more flexible input and output conditions.
In this library we use OpenLayers as a visualization engine(Currently OSM is the base map). 
Also available is a basic web api which can be deployed.
At this moment the API communicates with an input of a SWMM inp file but that is changing to the standard defined above
We intend to introduce a simple form for taking that in with some sensible defaults.
We intend to provide an endpoint for retrieving a sample inp file.
