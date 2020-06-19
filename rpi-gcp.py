import smbus
import time

import os
from google.cloud import pubsub_v1


bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x04
a=100
vib=0
t=0
h=0

# Create an object for publishing
publisher = pubsub_v1.PublisherClient()

# Define topic path
topic_path = 'projects/{project_id}/topics/{topic}'.format(
    project_id=os.getenv('PROJECT_ID'), topic=os.getenv('TOPIC_NAME'))


def readNumber():
    number = bus.read_byte(address)
    # number = bus.read_byte_data(address, 1)
    return number
while True:    
    try:
        rep =bus.read_i2c_block_data(address,0)
        string = ""
        for i in range(0,12):
            string += chr(rep[i])
        try:
            string=string.split()
            t=float(string[0])    
            h=float(string[2])
                
            if((int(string[1])-a)<0):
                continue
            else:
                vib=(int(string[1])-a)/2
            print("t=",string[0],"*c","vib=",vib,"/s","h=",string[2],"%",)
            a=int(string[1])
            try:
                payload = '{{ "data":"PayloadData", "Timestamp":{}, \
"Temperature":{:3.2f}, \
"Humidity":{:3.2f}, \
"Vibrations":{:3.2f}}}'.format(int(time.time()), t, h,vib)

                # Publish the payload to the cloud
                publisher.publish(topic_path, data=payload.encode('utf-8'))

                print("Publishing the payload : " + payload)

            except:
                print("GCP error")
            
        except:
            print("split error")
            
        
    except:
        print("i2c error")

    
    time.sleep(1)
