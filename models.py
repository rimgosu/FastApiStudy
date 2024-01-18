from sqlalchemy import Column, TEXT, INT, BIGINT
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Chatbot(Base):
    __tablename__ = "chatbot"
    num = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
    type = Column(TEXT, nullable=False)
    msg = Column(TEXT, nullable=False)