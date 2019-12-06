#!/usr/bin/env python

'''MyOpen3d'''

from farmware_tools import device
import hellow_message as hm

message = hm.hellow()
#print(message)

device.log(message='{}'.format(message))
