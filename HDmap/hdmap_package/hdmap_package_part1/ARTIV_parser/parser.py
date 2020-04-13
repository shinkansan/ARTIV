#OSM Parser임
# osmnx 같은 osm 전용 툴이 있지만, geojson으로 인식할 것임.

import geopandas as gpd
from shapely.geometry import LineString
import matplotlib.pyplot as pyplot
import numpy as np

class loadMap():
	def __init__(self, path):
		self.mapLoad = gpd.read_file(path)
		self.mapLoad = self.mapLoad.to_crs(epsg=32652)

	def getItem(self):
		return self.mapLoad




def main():
	autoStuff = loadMap("as.geojson")





if __name__ == "__main__":
	main()
	mapfile = autoStuff.getItem()