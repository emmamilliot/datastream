# datastream
M2 DS S2 data stream (with River, Kafka..)


## KAFKA requirements

Download - Scala 2.12 https://dlcdn.apache.org/kafka/3.1.0/kafka_2.12-3.1.0.tgz

$ tar -xzf kafka_2.13-2.7.0.tgz 

$ cd kafka_2.13-2.7.0

Edit : config/zookeeper.properties

Execute : $ bin/zookeeper-server-start.sh config/zookeeper.properties (keep a shell running on this query)

Edit : config/server.properties

Execute : bin/kafka-server-start.sh config/server.properties (keep a shell running on this query)

Create a topic named yfinanceapi: bin/kafka-topics.sh --create --topic yfinanceapi --bootstrap-server localhost:9092


## Yfinance library 

Read the doc : https://pypi.org/project/yfinance/

$ pip install yfinance
