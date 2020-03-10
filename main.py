from variables import webex_bot as bot
import teams_functions
from flask import Flask, request
from SQL_helper_functions import DatabaseManager


app = Flask(__name__)

@app.route('/newmessage', methods=['POST'])
def new_message():

    json_data = request.json

    message_id = json_data["data"]["id"]
    room_id = json_data["data"]["roomId"]

    message = teams_functions.get_message(message_id, bot.token)
    print(room_id)
    print(message)

    # I would like to show the operational data of my interfaces
    if message == "CaptainBuzz How's the weather?":
        dbObj = DatabaseManager()
        Latest_temp = dbObj.read_db_record("SELECT Temperature FROM DHT11_Temperature_Data ORDER BY id DESC LIMIT 1")[0][0]
        Latest_hum = dbObj.read_db_record("SELECT Humidity FROM DHT11_Humidity_Data ORDER BY id DESC LIMIT 1")[0][0]
        TimeStamp = dbObj.read_db_record("SELECT Date_n_Time FROM DHT11_Humidity_Data ORDER BY id DESC LIMIT 1")[0][0]
        print("Temperature= "+ Latest_temp + ' °C Humidity= ' + Latest_hum + ' % Time Stamp: ' + TimeStamp[:20])
        teams_functions.post_message_markdown(("I was hoping you'd ask me that! The current conditions in the hive are:<br/>Temp= "+ Latest_temp + ' °C<br/>Humidity= ' + Latest_hum + ' %<br/>Time Stamp: ' + TimeStamp[:20]), room_id, bot.token)
        del dbObj

    else:
        teams_functions.post_help_bot(room_id, bot.token)

    return "message sent"


@app.route('/newroom', methods=['POST'])
def new_room():

    json_data = request.json

    room_id = json_data["data"]["roomId"]
    print(room_id)
    teams_functions.post_message_markdown("Hey, I have been added to a new room !", room_id, bot.token)
    teams_functions.post_help_bot(room_id, bot.token)

    return "message sent"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
