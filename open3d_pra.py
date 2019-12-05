#!/usr/bin/env python
'''MyOpen3d'''

from farmware_tools import device, get_config_value, env
import cv2
import numpy as np
import os
import open3d as o3d

device.log(message='OK! Open3d', message_type='success')

#config = o3d.io.AzureKinectSensorConfig()
