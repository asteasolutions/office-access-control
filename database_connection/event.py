from database import DBConnection
from sqlalchemy.sql import select
from sqlalchemy import cast, Date
from db_modules import Events, Event_Names, Record_Names, Card_Holder


class Event(object):

    def __init__(self,eventID, eventType, eventTime, cardNumber, recordName):
        self.eventID = eventID
        self.eventType = eventType
        self.eventTime = eventTime
        self.cardNumber = cardNumber
        self.recordName = recordName

    def print_event(self):
        print("------------------")
        print("Event ID = {}".format(self.eventID))
        print("Event Type = {}".format(self.eventType))
        print("Event Time = {}".format(self.eventTime))
        print("Card Number = {}".format(self.cardNumber))
        print("Record Name = {}".format(self.recordName))
        
    @staticmethod
    def create_object_arr_by_result(result):
        events = []
        for row in result:
            eventID = row["Event ID"]
            eventType = row["EventName"]
            eventTime = row["Field Time"]
            cardNumber = row["Card Number"]
            recordName = row["Name"]
            events.append(Event(eventID, eventType, eventTime, cardNumber, recordName))

        return events

    @staticmethod
    def get_by_id(id):
        result = select([Events.id, Event_Names.name, Events.field_time, Card_Holder.card_num, Record_Names.name]).select_from(Events.__table__
            .join(Event_Names,Event_Names.event_type.like(Events.event_type))
            .join(Card_Holder,Card_Holder.id.like(Events.card_holder_id))
            .join(Record_Names,Record_Names.record_name_id.like(Events.record_name_id))).where(Events.id == id)

        rs = DBConnection.engine.execute(result)
        events = []
        for row in rs:
            events.append(Event(*row))
        return events

    @staticmethod
    def get_by_name(name):
        result = select([Events.id, Event_Names.name, Events.field_time, Card_Holder.card_num, Record_Names.name]).select_from(Events.__table__
            .join(Event_Names,Event_Names.event_type.like(Events.event_type))
            .join(Card_Holder,Card_Holder.id.like(Events.card_holder_id))
            .join(Record_Names,Record_Names.record_name_id.like(Events.record_name_id))).where(Event_Names.name == name)

        rs = DBConnection.engine.execute(result)
        events = []
        for row in rs:
            events.append(Event(*row))
        return events

    @staticmethod
    def get_by_date(date):
        result = select([Events.id, Event_Names.name, Events.field_time, Card_Holder.card_num, Record_Names.name]).select_from(Events.__table__
            .join(Event_Names,Event_Names.event_type.like(Events.event_type))
            .join(Card_Holder,Card_Holder.id.like(Events.card_holder_id))
            .join(Record_Names,Record_Names.record_name_id.like(Events.record_name_id))).where(cast(Events.field_time, Date) == date)

        rs = DBConnection.engine.execute(result)
        events = []
        for row in rs:
            events.append(Event(*row))
        return events

        

    @staticmethod
    def get_by_card_num(card_num):
        result = select([Events.id, Event_Names.name, Events.field_time, Card_Holder.card_num, Record_Names.name]).select_from(Events.__table__
            .join(Event_Names,Event_Names.event_type.like(Events.event_type))
            .join(Card_Holder,Card_Holder.id.like(Events.card_holder_id))
            .join(Record_Names,Record_Names.record_name_id.like(Events.record_name_id))).where(Card_Holder.card_num == card_num)

        rs = DBConnection.engine.execute(result)
        events = []
        for row in rs:
            events.append(Event(*row))
        return events

    @staticmethod
    def get_by_record_name(record_name):
        result = select([Events.id, Event_Names.name, Events.field_time, Card_Holder.card_num, Record_Names.name]).select_from(Events.__table__
            .join(Event_Names,Event_Names.event_type.like(Events.event_type))
            .join(Card_Holder,Card_Holder.id.like(Events.card_holder_id))
            .join(Record_Names,Record_Names.record_name_id.like(Events.record_name_id))).where(Record_Names.name == record_name)

        rs = DBConnection.engine.execute(result)
        events = []
        for row in rs:
            events.append(Event(*row))
        return events
            




