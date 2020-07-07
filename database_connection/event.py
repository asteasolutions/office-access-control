from database import DBConnection


class Event(object):

    def __init__(self,eventID, eventType, eventTime, cardNumber, recordName):
        self.eventID = eventID
        self.eventType = eventType
        self.eventTime = eventTime
        self.cardNumber = cardNumber
        self.recordName = recordName




