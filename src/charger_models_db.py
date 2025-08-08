from sqlalchemy import Column, Integer, DateTime, func, Float
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
    tma_0 = Column(Float)
    tma_1 = Column(float)

    def __str__(self):
        return f"StatusPollEntity: ({self.id}, {self.time}, {self.eto}, {self.err}, {self.tma_1}, {self.tma_2})"
