#Importing necessary modules
from kafka import KafkaProducer
import json
import time
import requests as req

#Function to get the data from Yahoo finance API
def get_data():
    try:
        url = "https://yfapi.net/v6/finance/quote"
        querystring = {"symbols":"AAPL,EURUSD=X"}
        headers = {'x-api-key': "wDvhQlo9Td9PuDs5Jbh5l6Z8lKoHtulRknt1y1Sh"}
        data = req.request("GET", url, headers=headers, params=querystring) 
        
        return data.json()
    except:
        print("Syantax error")

#Function to publish a message
def publish_message(producerkey,key,data_key):
    try:
        key_bytes = bytes(key, encoding='utf-8')
        producerkey.send("yfinanceapi", json.dumps(data[key]).encode('utf-8'), key_bytes)
        print('message_published')
    except:
        print("message not published")

#Function to declear connection to producer
def kafka_producer_connection():
    try:
        producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
        return producer
    except:
        print("Connection error")

#Declearing main function
while True:
    data = get_data()
    # print(len(data))
    if len(data) > 0:
        # print(data)
        kafka_producer = kafka_producer_connection()
        # print(len(data))
        for i,key in enumerate(sorted(data)):
            publish_message(kafka_producer,key, data[key])
            time.sleep(2)
