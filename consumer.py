#Importing modules
import json
from kafka import KafkaConsumer

#Declearing consumer connection
try:
    consumer = KafkaConsumer('yfinanceapi',bootstrap_servers=['localhost:9092'])
except:
    print('connection error')

#getting data and predicting result using the model
def stock_prediction():
        try:
            for msg in consumer:
                res = json.loads(msg.value.decode('utf-8'))
                print(res)
        except:
            print('Debug the above lines of code')
