from kafka import KafkaConsumer
consumer = KafkaConsumer( 'testTopic')
for message in consumer:
	values = message.value
	print(values)
