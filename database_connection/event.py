from database import DBConnection


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
        
        result = DBConnection.engine.execute(
            '''select [Event ID], [Event Names].Name as EventName, [Field Time], [Card Number], [Record Names].Name from Events
            left join [Event Names] on Events.[Event Type] = [Event Names].[Event Type]
            left join [Card Holder Names] on Events.[Card Holder ID] = [Card Holder Names].[Card Holder ID]
            left join [Record Names] on Events.[Record Name ID] = [Record Names].[Record Name ID]
            where [Event ID] = {}
            '''.format(id))

        return Event.create_object_arr_by_result(result)
        

    @staticmethod
    def get_by_name(name):
        result = DBConnection.engine.execute(
            '''select [Event ID], [Event Names].Name as EventName, [Field Time], [Card Number], [Record Names].Name from Events
            left join [Event Names] on Events.[Event Type] = [Event Names].[Event Type]
            left join [Card Holder Names] on Events.[Card Holder ID] = [Card Holder Names].[Card Holder ID]
            left join [Record Names] on Events.[Record Name ID] = [Record Names].[Record Name ID]
            where [Event Names].Name = '{}'
            '''.format(name))

        return Event.create_object_arr_by_result(result)

    @staticmethod
    def get_by_date(date):
        result = DBConnection.engine.execute(
            '''select [Event ID], [Event Names].Name as EventName, [Field Time], [Card Number], [Record Names].Name from Events
            left join [Event Names] on Events.[Event Type] = [Event Names].[Event Type]
            left join [Card Holder Names] on Events.[Card Holder ID] = [Card Holder Names].[Card Holder ID]
            left join [Record Names] on Events.[Record Name ID] = [Record Names].[Record Name ID]
            where [Field Time] = '{}'
            '''.format(date))

        return Event.create_object_arr_by_result(result)

    @staticmethod
    def get_by_card_num(card_num):
        result = DBConnection.engine.execute(
            '''select [Event ID], [Event Names].Name as EventName, [Field Time], [Card Number], [Record Names].Name from Events
            left join [Event Names] on Events.[Event Type] = [Event Names].[Event Type]
            left join [Card Holder Names] on Events.[Card Holder ID] = [Card Holder Names].[Card Holder ID]
            left join [Record Names] on Events.[Record Name ID] = [Record Names].[Record Name ID]
            where [Card Number] = '{}'
            '''.format(card_num))

        return Event.create_object_arr_by_result(result)

    @staticmethod
    def get_by_record_name(record_name):
        result = DBConnection.engine.execute(
            '''select [Event ID], [Event Names].Name as EventName, [Field Time], [Card Number], [Record Names].Name from Events
            left join [Event Names] on Events.[Event Type] = [Event Names].[Event Type]
            left join [Card Holder Names] on Events.[Card Holder ID] = [Card Holder Names].[Card Holder ID]
            left join [Record Names] on Events.[Record Name ID] = [Record Names].[Record Name ID]
            where [Record Names].Name = '{}'
            '''.format(record_name))

        return Event.create_object_arr_by_result(result)
            




