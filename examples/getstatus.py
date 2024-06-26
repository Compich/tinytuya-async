# TinyTuya Example
# -*- coding: utf-8 -*-
"""
 TinyTuya - Example to fetch status of Tuya device

 Author: Jason A. Cox
 For more information see https://github.com/jasonacox/tinytuya_async

"""
import tinytuya_async
import time

# Connect to the device - replace with real values
d=tinytuya_async.OutletDevice(DEVICEID, DEVICEIP, DEVICEKEY)
d.set_version(3.3)

# Alternative connection - for some devices with 22 character IDs they require a special handling
#    d=tinytuya_async.OutletDevice(DEVICEID, DEVICEIP, DEVICEKEY, 'device22')
#    d.set_dpsUsed({"1": None})
#    d.set_version(3.3)

# Option for Power Monitoring Smart Plugs - Some require UPDATEDPS to update power data points
# payload = d.generate_payload(tinytuya_async.UPDATEDPS,['18','19','20'])
# d.send(payload)
# sleep(1)

# Get the status of the device
# e.g. {'devId': '0071299988f9376255b', 'dps': {'1': True, '3': 208, '101': False}}
data = d.status()
print(data)
