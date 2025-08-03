from sqlalchemy import Column, Integer, DateTime, func
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import UUID
import uuid

from src.models_base import Base

class StatusPollEntity(Base):
    __tablename__ = "status_poll"
    # in code Column(DateTime, default=datetime.utcnow)
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)  #
    time = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    eto = Column(Integer)
    err = Column(Integer)

    def __str__(self):
        return f"StatusPollEntity: ({self.id}, {self.time}, {self.eto}, {self.err})"
