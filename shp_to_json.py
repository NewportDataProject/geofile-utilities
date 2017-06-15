import geopandas as gpd
import shapefile
import argparse
from epsg_codes import epsg

# use argparse for command line usage
parser = argparse.ArgumentParser()
parser.add_argument("shapefile", help="path to the shapefile to be converted")
parser.add_argument("geojsonfile", help="path to the output file")
parser.add_argument("-c", "--crs", help="EPSG code for coordinate reference system of the source shapefile. Default is 4326 for WGS84.")
args = parser.parse_args()


filepath = args.shapefile
outfile = args.geojsonfile  # TODO: this needs to be checked if the path exists or not, and create if not

# if crs isn't specified, default to WGS84
if args.crs:
    crs = epsg(args.crs)
else:
    crs = {'init': 'epsg:4326'}

reader = shapefile.Reader(filepath)

# Extract the column names for the data
fields = reader.fields[1:]
field_names = [field[0] for field in fields]

buffer = []
for sr in reader.shapeRecords():
    atr = dict(zip(field_names, sr.record))
    geom = sr.shape.__geo_interface__
    buffer.append(dict(type="Feature", geometry=geom, properties=atr))
geo_data = gpd.GeoDataFrame.from_features(buffer, crs=crs)

# Convert to WGS84
geo_data = geo_data.to_crs(crs={'init': 'epsg:4326'})

# The path specified in .to_file() needs to exist, otherwise fiona thrown an error.
geo_data.to_file(outfile, driver='GeoJSON')
