import os
from google.cloud import iot_v1
import RPi.GPIO as IO          #calling header file which helps us use GPIO’s of PI
import time                            #calling time to provide delays in program
IO.setwarnings(False)           #do not show any warnings
IO.setmode (IO.BCM)         #we are programming the GPIO by BCM pin numbers. (PIN35 as ‘GPIO19’)
IO.setup(19,IO.OUT)           # initialize GPIO19 as an output.
p = IO.PWM(19,100)          #GPIO19 as PWM output, with 100Hz frequency
p.start(0)
while True:
    client = iot_v1.DeviceManagerClient()
    device_path = client.device_path(
        project_id, cloud_region, registry_id, device_id)
    configs = client.list_device_config_versions(device_path)
    #for config in configs.device_configs:
    #print('version: {}\n\tcloudUpdateTime: {}\n\t data: {}'.format(config.version,config.cloud_update_time,config.binary_data))
    config=configs.device_configs
    intensity=config[0].binary_data.decode('ascii')
    print(intensity)
    p.ChangeDutyCycle(int(intensity))
