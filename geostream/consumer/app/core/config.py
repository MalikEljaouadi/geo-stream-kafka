# import sys

# from loguru import logger
from pydantic import BaseModel, Field

# import logging
# from app.core.logging import InterceptHandler


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

# Configure logging
# LOGGING_LEVEL = logging.DEBUG if consumer_config.DEBUG else logging.INFO
# logging.basicConfig(handlers=[InterceptHandler(level=LOGGING_LEVEL)], level=LOGGING_LEVEL)
# logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])
