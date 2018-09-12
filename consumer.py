Python 3.6.4 (v3.6.4:d48ecebad5, Dec 18 2017, 21:07:28) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
  GNU nano 2.5.3                        File: consumer-producer.py                                                        

import json, time
from kafka import KafkaConsumer, KafkaProducer
from kafka.errors import KafkaError
from random import uniform

consumer = KafkaConsumer(bootstrap_servers=['172.24.41.202:8080'],
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))
consumer.subscribe(pattern='bogota-.*.-.*.-.*.')

producer = KafkaProducer(bootstrap_servers=['172.24.41.202:8080'], 
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

    
