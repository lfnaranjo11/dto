import json, time
from kafka import KafkaConsumer, KafkaProducer
from kafka.errors import KafkaError
from random import uniform

consumer = KafkaConsumer(bootstrap_servers=['172.24.41.202:8081'],
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))
consumer.subscribe(pattern='bogota-.*.-.*.-.*.')

producer = KafkaProducer(bootstrap_servers=['172.24.41.202:8081'], 
             value_serializer=lambda v: json.dumps(v).encode('utf-8'))

temp_list1 = []
temp_list2 = []


for message in consumer:
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))

    if (message.value['place'] == "bogota"):
      temp_list1.append(message.value['value'])
    elif (message.value['place'] == "lima"):
      temp_list2.append(message.value['value'])

    
      temp_list1 = []

    
