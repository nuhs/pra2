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

device.log(message='OK!', message_type='success')

# Open the camera
camera = cv2.VideoCapture(0)
sleep(0.1)

# Take a photo
ret, image = camera.read()

# Close the camera
camera.release()

# Output
if ret:  # an image has been returned by the camera
    h, w, c = image.shape
    device.log('Image Size {}:{}.'.format(h,w))
    device.log('Image C {}.'.format(c))
    device.log('Image Color {}.'.format(image[1,1]))
    
else:  # no image has been returned by the camera
    device.log('Problem getting image from video{}.'.format(
        0), 'error', ['toast'])

if __name__ == '__main__':
    usb_camera_photo(0)


#config = o3d.io.AzureKinectSensorConfig()
