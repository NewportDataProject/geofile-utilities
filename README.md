# geofile-utilities
A collection of scripts to help work with GIS files by conversion, 
reference adjustment, and basic file management.

## shp_to_json.py
`python shp_to_json.py /path/to/shapefile /path/to/geojson --crs <source coordinate reference>`

## epsg_codes.py
Contains a list of useful but non-standard EPSG codes. Call `epsg(crs)` 
to get a dict of the Proj4 parameters, or return `{'init':'epsg:<crs>'}` to pass through to
other libraries without change.