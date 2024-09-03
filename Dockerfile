FROM registry.access.redhat.com/ubi9/python-311:1-72.1724040033

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/clickhouse_migrate/ ./

CMD ["python", "up.py"]