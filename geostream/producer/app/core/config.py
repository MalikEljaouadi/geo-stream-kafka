from pydantic import BaseModel, Field


class ProducerConfig(BaseModel):
    PROJECT_NAME: str = Field(default="geostream-kafka-producer", env="PROJECT_NAME")
    KAFKA_URI: str = Field(default="geo-stream-kafka_kafka_1", env="KAFKA_URI")
    KAFKA_PORT: str = Field(default="9092", env="KAFKA_PORT")
    DEBUG: bool = Field(default=False, env="DEBUG")


# Initialize the ProducerConfig class
producer_config = ProducerConfig()

# Kafka_broker URL
KAFKA_INSTANCE = producer_config.KAFKA_URI + ":" + producer_config.KAFKA_PORT
