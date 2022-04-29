from pydantic import BaseModel, Field


# Class containing the env vars of the consumer
class ConsumerConfig(BaseModel):
    PROJECT_NAME: str = Field(default="geostream-kafka-consumer", description="name of the project", env="PROJECT_NAME")
    KAFKA_URI: str = Field(default="geo-stream-kafka_kafka_1", env="KAFKA_URI")
    KAFKA_PORT: str = Field(default="9092", env="KAFKA_PORT")
    DEBUG: bool = Field(default=False, env="DEBUG")


# Initialize the ConsumerConfig class
consumer_config = ConsumerConfig()

# Kafka URL
KAFKA_INSTANCE = consumer_config.KAFKA_URI + ":" + consumer_config.KAFKA_PORT
