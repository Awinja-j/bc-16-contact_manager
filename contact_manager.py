from conn import Contact, Message
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from twilio.rest import TwilioRestClient

Base = declarative_base()
engine = create_engine('sqlite:///contact.db')
Session = sessionmaker(bind=engine)
session = Session()

#  use env variable to hide token
account_sid = 'ACc684e833e5afc573a4cccee306537e95'
auth_token = '8d835935196f549c04527d55adeac603'


class ContactManager(object):
    def add(self, name, phonenumber):
        """
        this adds name and phone number into db.
        if phone number is added without name, you get error.
        if name is added without phone number,you get error
        if phone number already exists, you get error
        if details are added succesfully, you get a succes notification

        """
        numbers = session.query(Contact).all()
        exists = False
        for i in numbers:
            if str(i.phone_number) == phonenumber:
                exists = True

        if not exists:
            details = Contact(phone_number=phonenumber, full_name=name.lower())
            session.add(details)
            session.commit()
            return ('Details saved succesfully!!')
        else:
            return "Number already in use"

    def search(self, fullname):
        """
        this performs a db search and returns a number if available
        and an error if not. If number is available, it is displayed
        and user is asked for the next action on number which can
        either be text or delete
        """

        full_name = fullname
        name = session.query(Contact).filter(
            Contact.full_name.contains(full_name.lower())).all()
        if len(name) > 1:
            for i in name:
                print ('[' + str(i.id) + '] ' + i.full_name + '\n')
            value = raw_input("which " + full_name + ":")
            for i in name:
                if i.id is int(value):
                    return(i.full_name + " " + str(i.phone_number))
        elif len(name) == 1:
            return((name[0].full_name + " " + str(name[0].phone_number)))
        else:
            return("Person not found!!")

    def text(self, name, messages):
        """ this saves texts into db"""
        client = TwilioRestClient(account_sid, auth_token)
        confirm = session.query(Contact).filter(
             Contact.full_name.contains(name.lower())).all()
        if len(confirm) > 1:
            for i in confirm:
                print('[' + str(i.id) + ']' + i.full_name +
                    ' ' + str(i.phone_number) + '\n')
            print(type(name), name)
            g = raw_input('Which ' + name + ': ')
            for i in confirm:
                if i.id is int(g):
                    client.messages.create(
                        to=("+" + str(i.phone_number)),
                        from_='+14026206866',
                        body=messages)
                    msg = Message(full_name=name, phone_messages=messages)
                    session.add(msg)
                    session.commit()
            return ('Message saved  and sent succesfully!!!')
        elif len(confirm) == 1:
            client.messages.create(
                to=("+" + str(confirm[0].phone_number)),
                from_='+14026206866',
                body=messages)
            msg = Message(full_name=name, phone_messages=messages)
            session.add(msg)
            session.commit()
            return ('Message saved  and sent succesfully!!!')
        else:
            return ('Person not found!!!')


c_manager = ContactManager()
