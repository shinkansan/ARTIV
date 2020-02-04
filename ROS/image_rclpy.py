import rclpy
import rclpy.node as node
import cv2
import numpy as np
import sensor_msgs.msg as msg
from sensor_msgs.msg import CompressedImage
import line_fit_video as lf
import keras
import tensorflow

class TestDisplayNode(node.Node):
    def __init__(self):
        super().__init__('IProc_TestDisplayNode')
        self.__window_name = "img"
        self.sub = self.create_subscription(CompressedImage,
        '/simulator/main_camera', self.msg_callback)
        print('init')
        # model load maskrcnn

    def msg_callback(self, img : CompressedImage):
        c = np.fromstring(bytes(img.data), np.uint8)
        #print(c.shape)

        image = cv2.imdecode(c, cv2.IMREAD_COLOR)
        #image = np.transpose(image, (1, 0, 2))
        #print(image.shape)
        self.display(image)


    def display(self, img):
        #print(img.shape)
        #img = lf.annotate_image(img)
        img = cv2.resize(img, dsize=None, fx=0.5, fy=0.5)
        #print(img.shape)
        #### your playgroud

        # model.predict(img) -> masked array
        # overlay it!
        # class -> person ! -> wd;->
        # done!

        cv2.imshow(self.__window_name, img)
        cv2.waitKey(1)

def main():
    #ros_core = ros.RclpyWrapper()
    rclpy.init()
    node = TestDisplayNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
