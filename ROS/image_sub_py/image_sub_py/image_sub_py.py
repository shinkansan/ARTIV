import cv2
import rclpy
import numpy as np

from std_msgs.msg import String
from std_msgs.msg import Float64
from sensor_msgs.msg import JointState
from sensor_msgs.msg import Image

def image_callback(msg : Image):
	print("Image Received", str(msg.header.frame_id))
	c = np.fromstring(bytes(msg.data), np.uint8)

	print(msg, c)


	cv2.imshow("Image", c)

	if cv2.waitKey(10)==27 : exit(1)


def main(args = None):
	rclpy.init(args=None)

	node = rclpy.create_node('image_sub_py')

	sub = node.create_subscription(Image, '/center_camera/image_color', image_callback)

	rclpy.spin(node)

	node.destroy_node()
	rclpy.shutdown()


if __name__ == '__main__':
	main()
