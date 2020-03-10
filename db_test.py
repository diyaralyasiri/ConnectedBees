from SQL_helper_functions import DatabaseManager

# dbObj = DatabaseManager()
# # database_headings = dbObj.read_db_record("SELECT id, sensorid, Temperature FROM DHT11_Temperature_Data")
# # print(database_headings[:10])

# Latest_temp = dbObj.read_db_record("SELECT Temperature FROM DHT11_Temperature_Data ORDER BY id DESC LIMIT 1")
# print(Latest_temp[0][0])
# # print(type(Latest_temp.pop(0)))
# del dbObj


dbObj = DatabaseManager()
Latest_temp = dbObj.read_db_record("SELECT Temperature FROM DHT11_Temperature_Data ORDER BY id DESC LIMIT 1")[0][0]
Latest_hum = dbObj.read_db_record("SELECT Humidity FROM DHT11_Humidity_Data ORDER BY id DESC LIMIT 1")[0][0]
TimeStamp = dbObj.read_db_record("SELECT Date_n_Time FROM DHT11_Humidity_Data ORDER BY id DESC LIMIT 1")[0][0]
print("I was hoping you'd ask me that! The current conditions in the hive are:\nTemp= "+ Latest_temp + ' °C\nHumidity= ' + Latest_hum + ' %\nTime Stamp: ' + TimeStamp[:20])

del dbObj
