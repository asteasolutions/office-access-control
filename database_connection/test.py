from database import DBConnection
from event import Event

for i in Event.get_by_date('2019-11-11'):
    i.print_event()




