#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-23 上午11:33
# @Author  : MaybeShewill-CV
# @Site    : https://github.com/MaybeShewill-CV/lanenet-lane-detection
# @File    : test_lanenet.py
# @IDE: PyCharm Community Edition
"""
test LaneNet model on single image
"""
import argparse
import os.path as ops
import time

import cv2
import glog as log
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

import global_config
import lanenet
import lanenet_postprocess

CFG = global_config.cfg


def init_args():
    """

    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_path', type=str, help='The image path or the src image save dir')
    parser.add_argument('--weights_path', type=str, help='The model weights path')

    return parser.parse_args()


def args_str2bool(arg_value):
    """

    :param arg_value:
    :return:
    """
    if arg_value.lower() in ('yes', 'true', 't', 'y', '1'):
        return True

    elif arg_value.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Unsupported value encountered.')


def minmax_scale(input_arr):
    """

    :param input_arr:
    :return:
    """
    min_val = np.min(input_arr)
    max_val = np.max(input_arr)

    output_arr = (input_arr - min_val) * 255.0 / (max_val - min_val)

    return output_arr


def test_lanenet(image_path, weights_path):
    """

    :param image_path:
    :param weights_path:
    :return:
    """
    assert ops.exists(image_path), '{:s} not exist'.format(image_path)

    log.info('Start reading image and preprocessing')
    t_start = time.time()
    #image = cv2.imread(image_path, cv2.IMREAD_COLOR)\
    cap = cv2.VideoCapture(image_path)

    
    log.info('Image load complete, cost time: {:.5f}s'.format(time.time() - t_start))

    input_tensor = tf.placeholder(dtype=tf.float32, shape=[1, 256, 512, 3], name='input_tensor')

    net = lanenet.LaneNet(phase='test', net_flag='vgg')
    binary_seg_ret, instance_seg_ret = net.inference(input_tensor=input_tensor, name='lanenet_model')

    postprocessor = lanenet_postprocess.LaneNetPostProcessor()

    saver = tf.train.Saver()

    # Set sess configuration
    sess_config = tf.ConfigProto()
    sess_config.gpu_options.per_process_gpu_memory_fraction = CFG.TEST.GPU_MEMORY_FRACTION
    sess_config.gpu_options.allow_growth = CFG.TRAIN.TF_ALLOW_GROWTH
    sess_config.gpu_options.allocator_type = 'BFC'

    sess = tf.Session(config=sess_config)

    with sess.as_default():

        saver.restore(sess=sess, save_path=weights_path)

        while(True):
            ret, image = cap.read()
            if ret == False:
                break;

            image_vis = cv2.resize(image[:][300:600], (512, 256), interpolation=cv2.INTER_LINEAR)
            image = cv2.resize(image[:][300:600], (512, 256), interpolation=cv2.INTER_LINEAR)
            image = image / 127.5 - 1.0

            t_start = time.time()
            binary_seg_image, instance_seg_image = sess.run(
                [binary_seg_ret, instance_seg_ret],
                feed_dict={input_tensor: [image]}
            )
            t_cost = time.time() - t_start
            log.info('Single imgae inference cost time: {:.5f}s'.format(t_cost))

            t_start = time.time()
            postprocess_result = postprocessor.postprocess(
                binary_seg_result=binary_seg_image[0],
                instance_seg_result=instance_seg_image[0],
                source_image=image_vis
            )
            mask_image = postprocess_result['mask_image']

            for i in range(CFG.TRAIN.EMBEDDING_FEATS_DIMS):
                instance_seg_image[0][:, :, i] = minmax_scale(instance_seg_image[0][:, :, i])
            embedding_image = np.array(instance_seg_image[0], np.uint8)
            '''
            plt.figure('mask_image')
            plt.imshow(mask_image[:, :, (2, 1, 0)])
            plt.figure('src_image')
            plt.imshow(image_vis[:, :, (2, 1, 0)])
            plt.figure('instance_image')
            plt.imshow(embedding_image[:, :, (2, 1, 0)])
            plt.figure('binary_image')
            plt.imshow(binary_seg_image[0] * 255, cmap='gray')
            plt.show()
            '''
            t_cost = time.time() - t_start
            log.info('Single imgae processing time: {:.5f}s'.format(t_cost))
            tempImg = binary_seg_image[0] * 255
            tempImg = np.array(tempImg).astype(np.uint8)
            cv2.imshow('mask_image',mask_image)
            cv2.imshow('org_image',image_vis)
            cv2.imshow('binary_image',tempImg )
            cv2.imshow('emb_image', embedding_image )
            if (cv2.waitKey(1) & 0xFF==27):
                break

    sess.close()

    return


if __name__ == '__main__':
    """
    test code
    """
    # init args
    args = init_args()

    test_lanenet(args.image_path, args.weights_path)
