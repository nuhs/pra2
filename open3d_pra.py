#!/usr/bin/env python
'''MyOpen3d'''

from farmware_tools import device, get_config_value, env
import cv2
import numpy as np
import os
import sys
import datetime
from time import time, sleep
#import pandas
#import matplotlib
#import open3d as o3d
#import pykinect

device.log(message='{OK!}', message_type='success')
# Open the camera
p = os.getenv('camera', 'USB')
camera = cv2.VideoCapture(0)
sleep(0.1)
#device.log(message='{}'.format(p), message_type='info')

epoch = int(time())
filename = '{timestamp}.jpg'.format(timestamp=epoch)
images_dir = env.Env().images_dir or '/tmp/images'
if not os.path.isdir(images_dir):
    device.log('{} directory does not exist.'.format(images_dir), 'error')
path = images_dir + os.sep + filename
discard_frames = 10
for _ in range(discard_frames):
  camera.grab()

# Take a photo
ret, image = camera.read()
# Close the camera
camera.release()

if ret:  # an image has been returned by the camera
    filename_path = upload_path(image_filename())
    # Save the image to file
    cv2.imwrite(filename_path, image)
    print('Image saved: {}'.format(filename_path))
else:  # no image has been returned by the camera
    device.log('Problem getting image from video{}.'.format(
        camera_port), 'error', ['toast'])
if ret:
  h, w, c = image.shape
  device.log(message='h={},w={}'.format(h,w), message_type='info')
  device.log(message='c={}'.format(c), message_type='info')

#config = o3d.io.AzureKinectSensorConfig()
