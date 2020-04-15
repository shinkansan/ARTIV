import rclpy
import matplotlib.pyplot as plt
import numpy as np
import osmnx as ox, networkx as nx, geopandas as gpd
from shapely.geometry import LineString
import shapely
from rclpy.qos import QoSHistoryPolicy, QoSProfile
from tf2_msgs.msg import TFMessage
from geometry_msgs.msg import TransformStamped
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
from geometry_msgs.msg import Point, Vector3
from std_msgs.msg import ColorRGBA
import copy
from hdmap_msg.msg import HdmapMarker, HdmapArray

class loadMap():
	def __init__(self, path):
		self.mapLoad = gpd.read_file(path)
		self.mapLoad = self.mapLoad.to_crs(epsg=32652)

	def getItem(self):
		return self.mapLoad


class hdmapMarkerFrame(HdmapMarker):
	def __init__(self):

		self.ns = "NAMESPACE"
		self.id = 0
		self.type = 3

	def frame(self):
		pass


	def encapsule(self):
		pass


	def __str__(self):
		return str([self.id, self.type])


	def to_msg(self):
		return self

def main():
	rclpy.init()
	node = rclpy.create_node('HDMAP_Server')
	qos_profile = QoSProfile(depth=1)
	qos_profile.history = QoSHistoryPolicy.RMW_QOS_POLICY_HISTORY_KEEP_LAST

	#hdmap_pub = node.create_publisher(HdmapMarker, 'hdmap_marker')
	hdmapA_pub = node.create_publisher(HdmapArray, 'hdmap_array')

	dgistMap = loadMap("dgist_a1.geojson").getItem()
	dgistMap = dgistMap.fillna('nodata') 

	curb = dgistMap.loc[dgistMap['type'] == HdmapMarker.CURB]
	whiteline = dgistMap.loc[dgistMap['type'] == HdmapMarker.WHITELINE]
	dgistMap.loc[dgistMap['type'] == HdmapMarker.TRAFFICSIGN]

	hdmap_array = HdmapArray()
	hdmap_array.array = []


	ros_time = node.get_clock().now().to_msg()
	featuredMap = dgistMap.loc[dgistMap['type'] != 'Feature']

	dataLen = len(featuredMap)
	for idx in range(0, dataLen):
		data = featuredMap.iloc[idx]
		marker = HdmapMarker()
		marker.id = idx
		marker.scale = Vector3(x=0.2, y=0.2, z=0.2)
		print(data)
		marker.type = int(data['type'])
		marker.header.stamp = ros_time

		# TODO: support another specific type
		try:
			if marker.type == marker.TRAFFICSIGN:
				coord_x, coord_y = data['geometry'].xy
				marker.pose = Point(x=float(coord_x), y=float(coord_y))
			else:
				marker.points = []
				coord_x, coord_y = data['geometry'].xy
				for lat, lng in zip(coord_x, coord_x):
						marker.points.append(Point(x=float(lat), y=float(lng)))
		except Exception:
			pass

		hdmap_array.array.append(marker)


	hdmap_array.header.stamp = ros_time
	import time
	while(1):
		hdmapA_pub.publish(hdmap_array)
		time.sleep(0.5)
		#rclpy.spin(node)
	





if __name__ == "__main__":

	main()




