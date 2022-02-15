from kafka import KafkaConsumer

consumer = KafkaConsumer('python-kafka')
for message in consumer:
    print (message)
