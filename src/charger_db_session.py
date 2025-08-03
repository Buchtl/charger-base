from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session as SessionType
import logging
from typing import Any

from src.models_base import Base
from src.charger_models_db import StatusPollEntity

class ChargerDbSession:
    logger = logging.getLogger("charger_base")
    session: SessionType

    def __init__(self, database_url: str = None):
        if database_url is None:
            database_url = "postgresql+psycopg2://charger:charger@pi4b:5432/charger"
        self.engine = create_engine(database_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = None

    def __enter__(self):
        self.session = self.Session()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if exc_type:
                self.session.rollback()
                self.logger.error(f"Rolling back due to exception: {exc_val}")
            else:
                self.session.commit()
                self.logger.info("Transaction committed successfully")
        finally:
            self.session.close()
            self.logger.info("Session closed")

    def write(self, data: Any):
        self.session.add(data)
        self.session.commit()
        self.logger.info(f"Added {data} to session")
