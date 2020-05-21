#!/usr/bin/env python

from prometheus_client import start_http_server, Counter, Gauge
from flask import Flask
import random
import time

# Counters can only increase
tf = Counter('jwnc_total_faults', 'Total number of faults recorded')
tf.inc(1)

# Gauges can change value up or down
es = Gauge('jwnc_equipment_status', 'Online/offline status', ['equipment_name'])
es.labels('litho1').set(0)
es.labels('vb6').set(1)

e24 = Gauge('jwnc_equipment_status_24hrs', 'Number of hours offline in the past 24hrs', ['equipment_name'])
e24.labels('litho1').set(2)
e24.labels('vb6').set(4)

start_http_server(8000)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

while True:
    tf.inc(1)
    es.labels('litho1').set(random.randint(0, 1))
    es.labels('vb6').set(random.randint(0, 1))
    e24.labels('litho1').set(random.randint(0, 3))
    e24.labels('vb6').set(random.randint(0, 3))
    time.sleep(5)