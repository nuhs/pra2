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

# Open the camera
camera = cv2.VideoCapture(0)
sleep(0.1)
device.log(message='{}'.format(capture), message_type='success')

#config = o3d.io.AzureKinectSensorConfig()
