from database import DBConnection
from event import Event


result = DBConnection.engine.execute(
    '''select [Event ID], [Event Names].Name as EventName, [Field Time], [Card Number], [Record Names].Name from Events
    left join [Event Names] on Events.[Event Type] = [Event Names].[Event Type]
    left join [Card Holder Names] on Events.[Card Holder ID] = [Card Holder Names].[Card Holder ID]
    left join [Record Names] on Events.[Record Name ID] = [Record Names].[Record Name ID]
    where [Event ID] = 69

    
    ''')
for row in result:
    eventID = row["Event ID"]
    eventType = row["EventName"]
    eventTime = row["Field Time"]
    cardNumber = row["Card Number"]
    recordName = row["Name"]
    print(eventID)
    print(eventType)
    print(eventTime)
    print(cardNumber)
    print(recordName)




