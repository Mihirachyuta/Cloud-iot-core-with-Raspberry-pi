# Cloud Iot core with Raspberry pi
This repository is to know how to connect your raspberry pi to google cloud IoT core. To do this you must have a project running in your in google cloud platform. For first time sign up, free $300 credits are also given.

## Steps
### Creating topic and subscription in pubsub
Enable the google cloud iot core api and pubsub api in your GCP console. Now you have to create pubsub topic and subscription
To create topic, open your cloud shell
```
gcloud pubsub topics create topic_name
```
To create subscription to the topic
```
gcloud pubsub subscriptions create –topic topic_name subscription_name
```
You can change “topic_name ” and “subscription_name” with your own names.
### Creating registry and device in IoT Core
Now, create a registry by going to IoT core in your console. Give an id to the registry and choose the nearest region and make sure you select the right topic. 
And in advanced option make sure you have MQTT selected.
<p align="center">
  <img src="registry.jpg">
</p>

Now go to the created registry and go to devices. Create a device and give it device id.
You can set authentication while creating a device. You can use the command in your computer
```
openssl genrsa -des3 -out private.pem 2048
openssl rsa -in private.pem -outform PEM -pubout -out public.pem
```
Now open the public key in a text editor and copy paste the public key including the begin and end lines and paste it in the console.
### Creating a service account
Now create a service account by navigating into the IAM and admin section. Give a name to the service account and give cloud IoT admin and pubsub admin roles.
<p align="center">
  <img src="service account.jpg">
</p>
Before completing creation of service account create key and save in your computer in json format.
Transfer this service account key to your raspberry pi.

### Package installations for raspberry pi
Now in your Raspberry pi, create a virtual environment using command in Raspberry pi command shell
```
python3 -m venv env
```
Activate the virtual environment created
```
Source ./env/bin/activate
```
Install the following packages
```
pip3 install cryptography
pip3 install paho-mqtt
pip3 install pyjwt
```

Now export the folloing as global variables projectId, topic and json key filepath
```
export PROJECT_ID=”projectid”
export TOPIC=”topic_name”
export CREDENTIALS=”file path”
```
Now install google cloud iot core and pubsub apis
```
pip3 install google-cloud-iot
pip3 install google-cloud-pubsub
```
### Running the code
Now download the demo.py file to use it and send your data to the cloud iot core.
```
python3 demo.py
```
Open subscription in pubsub, then open view messages and click pull.
You must see the “hello world” message we sent.

