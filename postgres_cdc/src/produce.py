from kafka import KafkaProducer
import json

# Kafka Configuration
KAFKA_BROKER = 'localhost:19092'  # Replace with your broker address
TOPIC_NAME = 'stock_sample'

# Create Kafka producer
producer = KafkaProducer(
    bootstrap_servers=[KAFKA_BROKER],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Example Stock 
stock_trade = {
  "trade_id": "TR123456",
  "timestamp": "2024-08-29T10:30:00Z",
  "account_id": "ACC987654",
  "symbol": "AAPL",
  "trade_type": "buy",
  "quantity": 100,
  "price_per_share": 180.50,
  "total_value": 18050.00,
  "commission": 7.00,
  "net_total": 18057.00,
  "status": "executed",
  "order_type": "limit",
  "limit_price": 180.50,
  "execution_time": "2024-08-29T10:30:01Z",
  "settlement_date": "2024-09-01",
  "broker": {
    "broker_id": "BR456789",
    "name": "XYZ Brokerage"
  }
}

# Send xAPI message to Kafka topic
producer.send(TOPIC_NAME, value=stock_trade)
producer.flush()

print(f"Sent stock_trade message: {stock_trade}")

# Close the producer connection
producer.close()

