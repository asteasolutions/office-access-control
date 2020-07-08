from database import DBConnection
from event import Event
from sqlalchemy.sql import select

s = select(['Events.[Event ID]'])
result = DBConnection.conn.execute(s)


# for i in Event.get_by_date('2019-11-11'):
#     i.print_event()




