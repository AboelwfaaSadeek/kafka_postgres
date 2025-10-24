import os
from kafka import KafkaProducer
import json
import time
import random

KAFKA_BROKERS = os.environ.get('KAFKA_BOOTSTRAP_SERVERS', 'kafka:9092') 
broker_list = KAFKA_BROKERS.split(',')

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

try:
    producer = KafkaProducer(
        bootstrap_servers=broker_list,
        value_serializer=json_serializer
    )
    print(f"🚀 Kafka Producer connected {broker_list}")
except Exception as e:
    print(f"❌Error: {e}")
    exit(1)


def create_order():
    return {
        "order_id": random.randint(10000, 99999),
        "customer_name": random.choice(["Ali", "Sara", "Omar", "Lina", "Youssef", "Aisha"]),
        "amount": round(random.uniform(10.50, 999.99), 2), 
        "status": random.choice(["pending", "confirmed", "shipped", "delivered"])
    }

if __name__ == "__main__":
    print("🚀 Streaming Producer started... sending orders every 2 seconds")
    while True:
        order = create_order()
        
        try:
            producer.send('orders', value=order)
            print(f"📤 Sent: {order}")
        
        except Exception as e:
            print(f"Error: {e}")
            
        time.sleep(2) 