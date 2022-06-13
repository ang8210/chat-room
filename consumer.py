from kafka import KafkaConsumer

TOPIC_NAME = 'items'

consumer = KafkaConsumer(TOPIC_NAME)
for msg in consumer:
    print(msg)