from database import DBConnection
from event import Event

for i in Event.get_by_record_name('Administration Console'):
    i.print_event()




