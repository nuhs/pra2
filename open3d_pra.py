#!/usr/bin/env python

import numpy as np
import open3d as o3d
import os
from time import time, sleep
import cv2
from farmware_tools import device, get_config_value, env

def image_filename():
    'Prepare filename with timestamp.'
    epoch = int(time())
    filename = '{timestamp}.jpg'.format(timestamp=epoch)
    return filename

def upload_path(filename):
    'Filename with path for uploading an image.'
    images_dir = env.Env().images_dir or '/tmp/images'
    if not os.path.isdir(images_dir):
        device.log('{} directory does not exist.'.format(images_dir), 'error')
    path = images_dir + os.sep + filename
    return path

def usb_camera_photo(camera_port):
    'Take a photo using a USB camera.'
    # Settings
    discard_frames = 10  # number of frames to discard for auto-adjust

    # Check for camera
    if not os.path.exists('/dev/video' + str(camera_port)):
        print('No camera detected at video{}.'.format(camera_port))
        device.log('USB Camera at video{} not detected.'.format(
            camera_port), 'error', ['toast'])

    # Open the camera
    config = o3d.io.AzureKinectSensorConfig()
    
