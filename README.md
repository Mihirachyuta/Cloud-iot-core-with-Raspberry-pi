# Cloud Iot core with Raspberry pi
This repository is to know how to connect your raspberry pi to google cloud IoT core. To do this you must have a project running in your in google cloud platform. For first time sign up, free $300 credits are also given.

## Steps
### Creating topic and subscription in pubsub
Enable the google cloud iot core api and cloud pubsub api in your GCP console. Now you have to create pubsub topic and subscription
To create topic, open your cloud shell
```
gcloud pubsub topics create topic_name
```
To create subscription to the topic
```
gcloud pubsub subscriptions create –topic topic_name subscription_name
```
