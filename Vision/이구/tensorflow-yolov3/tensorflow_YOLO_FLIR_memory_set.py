#! /usr/bin/env python
# coding=utf-8
#================================================================
#   Copyright (C) 2018 * Ltd. All rights reserved.
#
#   Editor      : VIM
#   File name   : video_demo.py
#   Author      : YunYang1994
#   Created date: 2018-11-30 15:56:37
#   Description :
#
#================================================================

import cv2
import time
import numpy as np
import core.utils as utils
import tensorflow as tf
from PIL import Image
import EasyPySpin
import PySpin
import argparse
import datetime
import gc


gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction = 0.333)
config = tf.ConfigProto(gpu_options=gpu_options)
config.gpu_options.allow_growth = True

return_elements = ["input/input_data:0", "pred_sbbox/concat_2:0", "pred_mbbox/concat_2:0", "pred_lbbox/concat_2:0"]
pb_file         = "./yolov3_coco.pb"
#video_path      = "./docs/images/road.mp4"
video_path      = 1
num_classes     = 80
input_size      = 416
graph           = tf.Graph()
return_tensors  = utils.read_pb_return_tensors(graph, pb_file, return_elements)

cap = EasyPySpin.VideoCapture(0)
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--index", type=int, default=0, help="Camera index (Default: 0)")
parser.add_argument("-e", "--exposure",type=float, default=-3, help="Exposure time [us] (Default: Auto)")
parser.add_argument("-g", "--gain", type=float, default=-1, help="Gain [dB] (Default: Auto)")
parser.add_argument("-G", "--gamma", type=float, help="Gamma value")
parser.add_argument("-b", "--brightness", type=float, help="Brightness [EV]")
parser.add_argument("-f", "--fps", type=float, help="FrameRate [fps]")
parser.add_argument("-s", "--scale", type=float, default=1, help="Image scale to show (>0) (Default: 0.25)")
args = parser.parse_args()
print("==========CAMERA SETTING==========")
print("camera idx: ",args.index)
print("exposure: ", args.exposure)
print("gain: ", args.gain)
print("gamma: ", args.gamma)
print("brightness: ", args.brightness)
print("frame rate: ",cap._get_FrameRate())
print("scale: ",args.scale)
print("WIDTH, HEIGHT:",)
if not cap.isOpened():
    print("Camera can't open\nexit")
    exit(-1)

cap.set(cv2.CAP_PROP_EXPOSURE, args.exposure) #-1 sets exposure_time to auto
cap.set(cv2.CAP_PROP_GAIN, args.gain) #-1 sets gain to auto
cap.cam.PixelFormat.SetValue(PySpin.PixelFormat_BayerGB8)

if args.gamma      is not None: cap.set(cv2.CAP_PROP_GAMMA, args.gamma)
if args.fps        is not None: cap.set(cv2.CAP_PROP_FPS, args.fps)
if args.brightness is not None: cap.set(cv2.CAP_PROP_BRIGHTNESS, args.brightness)

with tf.Session(config=config, graph=graph) as sess:
    while True:
        return_value, frame = cap.read()
        if return_value:
            frame = cv2.cvtColor(frame, cv2.COLOR_BayerGB2RGB)
            image = Image.fromarray(frame)

        else:
            raise ValueError("No image!")
        frame_size = frame.shape[:2]
        image_data = utils.image_preporcess(np.copy(frame), [input_size, input_size])
        image_data = image_data[np.newaxis, ...]
        #prev_time = time.time()

        pred_sbbox, pred_mbbox, pred_lbbox = sess.run(
            [return_tensors[1], return_tensors[2], return_tensors[3]],
                    feed_dict={ return_tensors[0]: image_data})

        pred_bbox = np.concatenate([np.reshape(pred_sbbox, (-1, 5 + num_classes)),
                                    np.reshape(pred_mbbox, (-1, 5 + num_classes)),
                                    np.reshape(pred_lbbox, (-1, 5 + num_classes))], axis=0)

        bboxes = utils.postprocess_boxes(pred_bbox, frame_size, input_size, 0.3)
        bboxes = utils.nms(bboxes, 0.45, method='nms')
        image = utils.draw_bbox(frame, bboxes)

        #curr_time = time.time()
        #exec_time = curr_time - prev_time
        result = np.asarray(image)
        #info = "time: %.2f ms" %(1000*exec_time)
        cv2.namedWindow("result", cv2.WINDOW_AUTOSIZE)
        #result = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        cv2.imshow("result", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): break

