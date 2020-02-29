import cv2
import rclpy
import numpy as np

from std_msgs.msg import String
from std_msgs.msg import Float64
from sensor_msgs.msg import JointState
from sensor_msgs.msg import Image

currentSpeed = 0.0

def image_callback(msg : Image):
	print("Image Received", str(msg.width), str(msg.height), str(msg.header.frame_id))
	print("Encoding Type:", str(msg.encoding))
	c = np.array(msg.data).astype(np.uint8)
	c = np.reshape(c, (msg.height, msg.width, -1))

	cv2.putText(c, "Speed: " + str(currentSpeed), (20, msg.height-30), 1, 1.8, (0,255,))
	
	cv2.imshow("Image", c)

	cv2.waitKey(1) 


def joint_callback(msg : JointState):
	global currentSpeed
	currentSpeed = msg.velocity[0]
	currentSpeed = np.round(currentSpeed, 6)

def main(args = None):
	rclpy.init(args=None)

	node = rclpy.create_node('image_sub_py')

	sub = node.create_subscription(Image, '/center_camera/image_color', image_callback)
	sub2 = node.create_subscription(JointState, '/vehicle/joint_states', joint_callback)

	rclpy.spin(node)

	node.destroy_node()
	rclpy.shutdown()


if __name__ == '__main__':
	main()
