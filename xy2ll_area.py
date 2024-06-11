from xy2ll import xy2ll
from ll2xy import ll2xy
import rasterio
import rasterio
import sys
from rasterio.plot import show
from rasterio.plot import show_hist
from rasterio.mask import mask
from pyproj import transformer
from pyproj import Transformer
import cv2
import numpy as np
np.set_printoptions(threshold=False)
import matplotlib.pyplot as plt
import glob
import ice
from functools import partial    
import shapely
import shapely.ops as ops
from shapely.geometry.polygon import Polygon
from shapely.ops import orient
from shapely import wkt #geod
from pyproj import Geod, CRS
from pyproj import Proj
from pyproj import Transformer


def lat_lon_area(coordinates):
    co={'type': 'Polygon', 'coordinates': [coordinates]}
    lon, lat = zip(*co['coordinates'][0])
    from pyproj import Proj
    pa = Proj("+proj=aea +lat_1=37.0 +lat_2=41.0 +lat_0=39.0 +lon_0=-106.55")
    x, y = pa(lon, lat)
    cop = {"type": "Polygon", "coordinates": [zip(x, y)]}
    from shapely.geometry import shape
    return shape(cop).area 

def xyll_area(coord):
    ll_coordinates=[] #creates list for converted lat/lon coordinates
    for i in coord:
        ll_coord = xy2ll(i[0], i[1], -1, 0,71)
        ll_coordinates.append(ll_coord)
    print(ll_coordinates)
    area = lat_lon_area(ll_coordinates)/1e+6
    print(area)

def ll_area(coordinates):
    co={'type': 'Polygon', 'coordinates': [coordinates]}
    lon, lat = zip(*co['coordinates'][0])
    from pyproj import Proj
    pa = Proj("+proj=aea +lat_1=37.0 +lat_2=41.0 +lat_0=39.0 +lon_0=-106.55")
    x, y = pa(lon, lat)
    cop = {"type": "Polygon", "coordinates": [zip(x, y)]}
    from shapely.geometry import shape
    return shape(cop).area
