FROM python:3.8-slim

WORKDIR /app

RUN pip install prometheus_client flask

COPY server.py /app/

CMD ["python", "/app/server.py"]
