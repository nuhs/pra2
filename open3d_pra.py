#!/usr/bin/env python
'''MyOpen3d'''

from farmware_tools import device, get_config_value, env
import cv2
import numpy as np
import os
import sys
import datetime
#import pandas
#import matplotlib
#import open3d as o3d
#import pykinect

device.log(message='{OK!}', message_type='success')
# Open the camera
p = os.getenv('camera', 'USB')
camera = cv2.VideoCapture(p)
sleep(0.1)
device.log(message='{OK!}', message_type='success')

# Take a photo
ret, image = camera.read()
if ret:
  h, w, c = image.shape

# Close the camera
camera.release()
device.log(message='h={},w={}'.format(h,w), message_type='success')
device.log(message='c={}'.format(c), message_type='success')

#config = o3d.io.AzureKinectSensorConfig()
