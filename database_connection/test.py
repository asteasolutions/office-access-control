from database import DBConnection



result = DBConnection.engine.execute("select * from Events where [Event ID] = 1")
for row in result:
    print("Time:", row['Field Time'])


print(DBConnection.engine)

