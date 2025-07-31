from sqlalchemy import Column, Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import UUID
import uuid

Base = declarative_base()

class User(Base):
    __tablename__ = 'status_poll'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    eto = Column(Integer)
    err = Column(Integer)

