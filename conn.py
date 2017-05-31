from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

engine = create_engine('sqlite:///contact.db')

Session = sessionmaker(bind=engine)

session = Session()


class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True, autoincrement=True)
    phone_number = Column(Integer, nullable=False)
    full_name = Column(String(255), nullable=False)


class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, nullable=False, primary_key=True)
    full_name = Column(String(255), nullable=False)
    phone_messages = Column(String(250), nullable=False)
    contacts = relationship(Contact)
    user_id = Column(Integer, ForeignKey('contacts.id'))


Base.metadata.create_all(engine)
