import rclpy
import EasyPySpin
import PySpin
import cv2
import argparse
from rclpy.node import Node
import sensor_msgs.msg as msg
from cv_bridge import CvBridge
import numpy as np

global args
class ImgPublisher(Node):
    def __init__(self):
        super().__init__('FLIR_ImgPublisher')
        self.publisher_ = self.create_publisher(msg.Image, 'FLIR_IMAGE')
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-i", "--index", type=int, default=0, help="Camera index (Default: 0)")
        self.parser.add_argument("-e", "--exposure",type=float, default=-3, help="Exposure time [us] (Default: Auto)")
        self.parser.add_argument("-g", "--gain", type=float, default=-1, help="Gain [dB] (Default: Auto)")
        self.parser.add_argument("-G", "--gamma", type=float, help="Gamma value")
        self.parser.add_argument("-b", "--brightness", type=float, help="Brightness [EV]")
        self.parser.add_argument("-f", "--fps", type=float, help="FrameRate [fps]")
        self.parser.add_argument("-s", "--scale", type=float, default=1, help="Image scale to show (>0) (Default: 0.25)")
        self.parser.add_argument('--width', dest='width', type = int, default = 2048)
        self.parser.add_argument('--height', dest='height', type = int, default = 1536)
        global args
        args = self.parser.parse_args()
        self.cap = EasyPySpin.VideoCapture(0)
        try:
            self.cap.set(cv2.CAP_PROP_EXPOSURE, args.exposure) #-1 sets exposure_time to auto
            self.cap.set(cv2.CAP_PROP_GAIN, args.gain) #-1 sets gain to auto
            self.cap.cam.PixelFormat.SetValue(PySpin.PixelFormat_BayerGB8)

            if args.gamma      is not None: self.cap.set(cv2.CAP_PROP_GAMMA, args.gamma)
            if args.fps        is not None: self.cap.set(cv2.CAP_PROP_FPS, args.fps)
            if args.brightness is not None: self.cap.set(cv2.CAP_PROP_BRIGHTNESS, args.brightness)

        except:
            if not self.cap.isOpened():
                self.get_logger().fatal("Camera can't open")
                exit(-1)

        print("==========CAMERA SETTING==========")
        print("camera idx: ",args.index)
        print("exposure: ", args.exposure)
        print("gain: ", args.gain)
        print("gamma: ", args.gamma)
        print("brightness: ", args.brightness)
        print("frame rate: ",self.cap._get_FrameRate())
        print("scale: ",args.scale)

    def img_callback(self):
        ret = msg.Image()
        while(1):

            if not self.cap.isOpened():
                print("Camera can't open\nexit")
                return -1

            ret, img = self.cap.read()
            img = cv2.cvtColor(img, cv2.COLOR_BayerGB2RGB)
            img = cv2.resize(img, dsize = (args.width, args.height))
            width, height, channels = img.shape
            #print("width: %d, height: %d" %(width,height))
            cv2.imshow("fuck_flir", img)


            temp=CvBridge().cv2_to_imgmsg(img, encoding = 'bgr8')


            #print(width, height)

            '''
            ret.data = temp.data
            ret.encoding = temp.encoding
            ret.header.frame_id = temp.header.frame_id
            ret.step = temp.step
            ret.height = height
            ret.width = width
            '''

            self.publisher_.publish(temp)

            key = cv2.waitKey(1)
            if key==ord("q"):
                break

def main(args=None):
    rclpy.init(args=args)
    image_publisher = ImgPublisher()
    image_publisher.img_callback()
    rclpy.spin(image_publisher)
    image_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
