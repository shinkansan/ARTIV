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

class loadMap():
	def __init__(self, path):
		self.mapLoad = gpd.read_file(path)
		self.mapLoad = self.mapLoad.to_crs(epsg=32652)

	def getItem(self):
		return self.mapLoad

class drawRviz():
	def __init__(self):
		'''
		rclpy.init(args=sys.argv)
		node = rclpy.create_node('OSMDrawer')
		qos_profile = QoSProfile(depth=1)
		qos_profile.history = QoSHistoryPolicy.RMW_QOS_POLICY_HISTORY_KEEP_LAST

		mapPub = node.create_publisher(MarkerArray, 'mapPub', qos_profile=qos_profile)
		'''
		pass

class transform_frame():
	def __init__(self):
		tf = TransformStamped()
		tf.header.frame_id = 'map'
		tf.child_frame_id = 'osmMap'
		tf.transform.translation = Vector3(x=0., y=0., z = 0.)

		tf.transform.rotation.w = 1.
		tf.transform.rotation.x = 0.
		tf.transform.rotation.y = 0.
		tf.transform.rotation.z = 0.
		self.tf = tf
	def publish(self, tfpublisher):
		tfpublisher.publish(TFMessage(transforms=[self.tf]))

class makerarray_frame(transform_frame):
	
	def __init__(self, node):
		self.cnt = 0
		self.node = node
		self.tf = transform_frame()
		self.output = MarkerArray()
		marker = Marker()
		marker.id = self.cnt
		
		marker.header.frame_id = 'osmMap' 
		marker.type = Marker.LINE_STRIP
		marker.action = Marker.ADD

		marker.scale = Vector3(x=1.8, y=.01, z=.01)
		marker.color = ColorRGBA(r=0.5, g=0., b=0.5, a=1.)
		marker.pose.position = Point(x=0.,y=0.,z=0.)
		marker.ns = 'Position'
		self.marker = marker

		self.marker.points = []

	def drawPoint(self, point, color=None):
		self.marker.points.append(point)
		self.marker.color = color if color else self.marker.color



	def appendMark(self):
		self.marker.id = self.marker.id + 1
		
		self.output.markers.append(copy.deepcopy(self.marker))

		self.marker.points = []

		
	def publish(self, mapPub, tfPub):
		#self.output.markers.append(self.marker)
		#self.tf.publish(tfPub)
		ros_time = self.node.get_clock().now()
		self.marker.header.stamp = ros_time.to_msg()
		#self.tf.tf.header.stamp = ros_time.to_msg()

		mapPub.publish(self.output)


def main():
	rclpy.init()
	node = rclpy.create_node('OSMDrawer')
	qos_profile = QoSProfile(depth=1)
	qos_profile.history = QoSHistoryPolicy.RMW_QOS_POLICY_HISTORY_KEEP_LAST

	tfPub = node.create_publisher(TFMessage, '/tf', qos_profile=qos_profile)
	mapPub = node.create_publisher(MarkerArray, 'mapPub', qos_profile=qos_profile)
	mapPub2 = node.create_publisher(MarkerArray, 'mapPub2', qos_profile=qos_profile)

	autoStuff = loadMap("AutonomouStuff_20191119_134123.geojson")
	mapfile = autoStuff.getItem()

	parkdf = mapfile.loc[mapfile['subtype'] == ('parking')]
	noparkdf = mapfile.loc[mapfile['subtype'] != ('parking')]



	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)

	#Marker Array
	marker_park = makerarray_frame(node)

	for part in parkdf.geometry:
		if type(part) == shapely.geometry.multilinestring.MultiLineString:
			for line in part:
				lat, lng = line.xy
				ax.plot(lat, lng, color='blue')
				for lat, lng in zip(lat, lng):
					print(lat, lng)
					marker_park.drawPoint(Point(x=lat, y=lng, z=0.),ColorRGBA(r=0.5, g=0.5, b=0.0, a=1.))
				marker_park.appendMark()

			continue
	            # https://gis.stackexchange.com/questions/104312/multilinestring-to-separate-individual-lines-using-python-with-gdal-ogr-fiona
		lat, lng = part.xy
		ax.plot(lat, lng, color='blue') 
		for lat, lng in zip(lat, lng):
			print(lat, lng)
			marker_park.drawPoint(Point(x=lat, y=lng, z=0.),ColorRGBA(r=0.5, g=0.5, b=0.0, a=1.))
		marker_park.appendMark()
		   
		
    


	marker_nopark = makerarray_frame(node)
	for part in noparkdf.geometry:
		if type(part) == shapely.geometry.multilinestring.MultiLineString:
			for line in part:
				lat, lng = line.xy
				ax.plot(lat, lng, color='green')
				for lat, lng in zip(lat, lng):
					marker_nopark.drawPoint(Point(x=lat, y=lng, z=0.))
				marker_nopark.appendMark()
				
			continue
	            # https://gis.stackexchange.com/questions/104312/multilinestring-to-separate-individual-lines-using-python-with-gdal-ogr-fiona
        
		lat, lng = part.xy
		ax.plot(lat, lng, color='green')
		for lat, lng in zip(lat, lng):
				marker_nopark.drawPoint(Point(x=lat, y=lng, z=0.))
		marker_nopark.appendMark()




	plt.show()

	while(rclpy.ok()):
		marker_nopark.publish(mapPub2, tfPub)
		marker_park.publish(mapPub, tfPub)

if __name__ == '__main__':
    main()
