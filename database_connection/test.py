from database import DBConnection
from event import Event
from sqlalchemy.sql import select
from db_modules import Events, Event_Names, Record_Names, Card_Holder

# find_it = select([Events.id, Event_Names.name, Events.field_time, Card_Holder.card_num, Record_Names.name]).select_from(Events.__table__
# .join(Event_Names,Event_Names.event_type.like(Events.event_type))
# .join(Card_Holder,Card_Holder.id.like(Events.card_holder_id))
# .join(Record_Names,Record_Names.record_name_id.like(Events.record_name_id))).where(Events.id == 15)
# print(str(find_it))


# rs = DBConnection.engine.execute(find_it)

# events = []

# for row in rs:
#     events.append(Event(*row))

# events[0].print_event()



# for i in Event.get_count_in_date('2019-11-11'):
#     i.print_event()

# print(Event.get_count_in_date('2019-11-11'))
# print(Event.get_left_count_in_date('2019-11-11'))
# print()


Event.make_graph_from_to('2019-11-4', '2019-11-11')


