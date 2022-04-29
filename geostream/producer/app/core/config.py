import sys

from loguru import logger
from pydantic import BaseModel, Field

import logging
from producer.app.core.logging import InterceptHandler


class ProducerConfig(BaseModel):
    PROJECT_NAME: str = Field(default="geostream-kafka-producer", env="PROJECT_NAME")
    KAFKA_URI: str = Field(default="0.0.0.0", env="KAFKA_URI")
    KAFKA_PORT: str = Field(default="9092", env="KAFKA_PORT")
    DEBUG: bool = Field(default=False, env="DEBUG")


# Initialize the ProducerConfig class
producer_config = ProducerConfig()

# Kafka_broker URL
KAFKA_INSTANCE = producer_config.KAFKA_URI + ":" + producer_config.KAFKA_PORT

# Logging setup
LOGGING_LEVEL = logging.DEBUG if producer_config.DEBUG else logging.INFO
logging.basicConfig(handlers=[InterceptHandler(level=LOGGING_LEVEL)], level=LOGGING_LEVEL)
logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])
