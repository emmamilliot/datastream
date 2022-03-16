#Importing necessary modules
from kafka import KafkaProducer
import json
import time
import pandas as pd
import requests as req
# https://pypi.org/project/yfinance/
import yfinance as yf


#Function to get the data from Yahoo finance API
def get_data(time_step):
    try:
      ticker_name = "AMZN"
      data = yf.Ticker(ticker_name)

      #Dans le cas où nous faisons la requête pour la première fois, pré-training du modèle avec toutes les valeurs de la journée
      #Cas à faire (non fonctionnel pour le moment)
      if time_step==0:
        hist = data.history(period='1d', interval='1m')
        return hist
      #Online learning : on prend la donnée en temps réelle, dernière donnée disponible
      else : 
        hist = pd.DataFrame(data.history(period='1d', interval='1m').iloc[-1])
        curr_dt = hist.columns[0]
        timestamp = (int(round(curr_dt.timestamp())))
        #from datetime import datetime
        #dt_object = datetime.fromtimestamp(timestamp)
        hist = hist.rename(columns={curr_dt : str(timestamp)})
        return hist.to_dict()

    except:
        print("Debug code")

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
i=1
while True:
    data = get_data(i)
    # print(data)
    # print(len(data))
    if len(data) > 0:
        # print(data)
        kafka_producer = kafka_producer_connection()
        # print(len(data))
        for i,key in enumerate(sorted(data)):
            publish_message(kafka_producer,key, data[key])
            time.sleep(60)
    i+=1