 
import json, time
from kafka import KafkaProducer
from kafka.errors import KafkaError
from random import uniform


producer = KafkaProducer(bootstrap_servers=['172.24.41.202:8081'], 
             value_serializer=lambda v: json.dumps(v).encode('utf-8'))

while True:
        producer.send('bogota-usaquen-longitud1-latitud1', {'time': time.strftime("%X"), 'measurement': 'sitio', 
                                        'value': round(uniform(20, 25),1), 'unit': 'cord', 'place': 'bogota'})
        producer.send('bogota-cahpinero-longitud3-latitud3', {'time': time.strftime("%X"), 'measurement': 'sitio', 
                                        'value': round(uniform(20, 25),1), 'unit': 'cord', 'place': 'bogota'}) 
        producer.send('lima-sanfernando-longitud4-latitud4', {'time': time.strftime("%X"), 'measurement': 'sitio', 
                                        'value': round(uniform(20, 25),1), 'unit': 'cord', 'place': 'lima'})                              



        producer.flush()
        time.sleep(5)


