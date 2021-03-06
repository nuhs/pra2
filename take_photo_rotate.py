#!/usr/bin/env python

'''Take a Photo'''

from farmware_tools import device, get_config_value, env
import hello_message as hm
import os
from time import time, sleep
import cv2
import numpy as np

message = hm.hello()
#print(message)

device.log(message='{}'.format(message))

def image_filename():
    'Prepare filename with timestamp.'
    epoch = int(time())
    filename = '{timestamp}.jpg'.format(timestamp=epoch)
    device.log('{}'.format(filename))
    return filename

def upload_path(filename):
    'Filename with path for uploading an image.'
    images_dir = env.Env().images_dir or '/tmp/images'
    if not os.path.isdir(images_dir):
        device.log('{} directory does not exist.'.format(images_dir), 'error')
    path = images_dir + os.sep + filename
    device.log('{}'.format(path))
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
    camera = cv2.VideoCapture(camera_port)
    sleep(0.1)

    # Let camera adjust
    for _ in range(discard_frames):
        camera.grab()

    # Take a photo
    ret, image = camera.read()
    h, w = image.shape[:2]
    angle = 270
    angle_rad = angle/180.0*np.pi
    w_rot = int(np.round(h*np.absolute(np.sin(angle_rad))+w*np.absolute(np.cos(angle_rad))))
    h_rot = int(np.round(h*np.absolute(np.cos(angle_rad))+w*np.absolute(np.sin(angle_rad))))
    size_rot = (w_rot, h_rot)
    center = (w/2, h/2)
    scale = 1.0
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
    affine_matrix = rotation_matrix.copy()
    affine_matrix[0][2] = affine_matrix[0][2] -w/2 + w_rot/2
    affine_matrix[1][2] = affine_matrix[1][2] -h/2 + h_rot/2

    image = cv2.warpAffine(image, affine_matrix, size_rot, flags=cv2.INTER_CUBIC)
    image = cv2.flip(image, 0)
    
    # Close the camera
    camera.release()

    # Output
    if ret:  # an image has been returned by the camera
        filename_path = upload_path(image_filename())
        # Save the image to file
        #cv2.imshow('frame', image)
        cv2.imwrite(filename_path, image)
        print('Image saved: {}'.format(filename_path))
    else:  # no image has been returned by the camera
        device.log('Problem getting image from video{}.'.format(
            camera_port), 'error', ['toast'])

if __name__ == '__main__':
    #CAMERA_PORT = get_config_value('multi-camera-take-photo', 'camera_port')
    usb_camera_photo(0)
