Python 3.6.4 (v3.6.4:d48ecebad5, Dec 18 2017, 21:07:28) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
GNU nano 2.5.3                           File: producer.py    
import json, time
from kafka import KafkaProducer
from kafka.errors import KafkaError
from random import uniform

producer = KafkaProducer(bootstrap_servers=['172.24.41.202:8$
                                                 value_seria$

while True:
        producer.send('bogota-usaquen-longitud1-latitud1', {'time': time.strftime("%X"), 'measurement': 'sitio', 
                                        'value': round(uniform(20, 25),1), 'unit': 'cord', 'place': 'bogota'})
        producer.send('bogota-cahpinero-longitud3-latitud3', {'time': time.strftime("%X"), 'measurement': 'sitio', 
                                        'value': round(uniform(20, 25),1), 'unit': 'cord', 'place': 'bogota'})
         producer.send('mexico-condesa-longitud2-latitud2', {'time': time.strftime("%X"), 'measurement': 'sitio', 
                                        'value': round(uniform(20, 25),1), 'unit': 'cord', 'place': 'mexico'}) 
        producer.send('lima-sanfernando-longitud4-latitud4', {'time': time.strftime("%X"), 'measurement': 'sitio', 
                                        'value': round(uniform(20, 25),1), 'unit': 'cord', 'place': 'lima'})                              



        producer.flush()
        time.sleep(5)


