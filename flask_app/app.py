from flask import Flask, jsonify, request, render_template, redirect, url_for
from ..database_connection.event import Event
import datetime

app = Flask(__name__)
app.debug = True
# app.config['SEND_FILE_MAX_AGE_DEFAULT']
clicked_date = ""


@app.route('/', methods=['GET'])
def main():
    return render_template("home.html")

@app.route('/date', methods=['GET'])
def date():
    clicked_date = request.args['res']
    cardsFound = Event.get_access_granted_in_date(clicked_date)
    cardsFound.sort(key = sortBy)
    for card in cardsFound:
        hours = str(card.eventTime).split(' ')
        card.eventTime = hours[1]
    print(clicked_date)
    return render_template("day.html", date=clicked_date, cardsCount = Event.get_count_in_date(clicked_date), cards = cardsFound)

@app.route('/real_time', methods=['GET', 'POST'])
def real_time():
    date = str(datetime.datetime.today()).split(' ')
    today = date[0]
    cardsFound = Event.get_access_granted_in_date(today)
    cardsFound.sort(key = sortBy)
    peoplePresent = Event.get_count_in_date(today) - Event.get_left_count_in_date(today)
    for card in cardsFound:
        hours = str(card.eventTime).split(' ')
        card.eventTime = hours[1]
    print(today)
    return render_template("real_time.html", event_date = today, date=today, cardsCount = Event.get_count_in_date(today), cards = cardsFound, peoplePresent = peoplePresent)

@app.route('/calendar', methods=['GET', 'POST'])
def calendar():
    return render_template("calendar.html")

def sortBy(card):
    return card.eventTime

if __name__=='__main__':
    app.run(debug=True)