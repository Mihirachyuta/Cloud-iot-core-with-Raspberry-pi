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
### Creating regisstry and device in IoT Core
Now, create a registry by going to IoT core in your console. Give an id to the registry and choose the nearest region and make sure you select the right topic. 
And in advanced option make sure you have MQTT selected.
Now go to the created registry and go to devices. Create a device and give it device id.
You can set authentication while creating a device. You can use the command in your computer
```
openssl genrsa -des3 -out private.pem 2048
openssl rsa -in private.pem -outform PEM -pubout -out public.pem
```
Now open the public key in a text editor and copy paste the public key including the begin and end lines and paste it in the console.
