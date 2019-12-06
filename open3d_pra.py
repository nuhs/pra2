#!/usr/bin/env python

'''MyOpen3d'''

from farmware_tools import device
import hello_message as hm

message = hm.hello()
#print(message)

device.log(message='{}'.format(message))
