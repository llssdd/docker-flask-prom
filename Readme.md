# Basic docker prometheus example

You should be able to run :
```
docker-compose up --build
```
And wait a while... The you can go to http://localhost:8000 to see the bare metrics, http://localhost:9090 to see prometheus
and http://localhost:3000 to get into grafana ('admin' / 'admin').

Inside grafana you need to add a 'data source' for prometheus.  The URL will be http://prometheus:9090 .  There is an example dashboard you should
be able to import into grafana once the 'prometheus' data source is created `basic-dashboard.json`.
