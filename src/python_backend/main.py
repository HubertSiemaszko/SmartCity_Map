import codecs
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import pandas as pd
from geopy.geocoders import Nominatim
import json

app = Nominatim(user_agent="tutorial")
url = "https://www.trojmiasto.pl/imprezy/kalendarz-imprez/dni,7dni,o1,0,offset,120.html"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

places = soup.find_all(class_="event__item__location")
names = soup.find_all(class_="event__item__title__name")
calendar=soup.find_all(class_="calendar-icon__icon")
hours=soup.find_all(class_="event__item__content__contain__info")

month_map = {
    "sty": "01", "lut": "02", "mar": "03", "kwi": "04",
    "maj": "05", "cze": "06", "lip": "07", "sie": "08",
    "wrz": "09", "paź": "10", "lis": "11", "gru": "12"
}

events = []

placeArray=[];
eventArray=[];
monthArray=[];
dayArray=[];
hoursArray=[];
longitudeArray=[];
latitudeArray=[];
dateTimeArray=[];

for i in range(20):
    try:
        eventPlace = places[i].find(class_="event__item__location__place").get_text()
        placeArray.append(eventPlace)

        eventName= names[i].find(class_="event__item__title").get_text()
        eventArray.append(eventName)

        eventMonth = calendar[i].find(class_="calendar-icon__icon__month").get_text()

        eventDay = calendar[i].find(class_="calendar-icon__icon__day").get_text()
        eventDay = eventDay.zfill(2)

        eventHour= hours[i].find(class_="event__item__date__hour").get_text()
        eventHour = eventHour.replace(' ', '').replace('\xa0', '').replace('godz.', '').replace(',', '').replace(' ', '').replace('.', ':')

        month_num = month_map[eventMonth]
        date_str = f"2025-{month_num}-{eventDay} {eventHour}"
        try:
            timestamp = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
        except ValueError as ve:
            print(f"Error parsing date '{date_str}':", ve)
            timestamp = None
        print(timestamp)
        print(placeArray[i]+" Gdańsk")
        eventLatitude = app.geocode(placeArray[i]+" Gdańsk").latitude
        latitudeArray.append(eventLatitude)
        eventLongitude=app.geocode(placeArray[i]+" Gdańsk").longitude
        longitudeArray.append(eventLongitude)

        events.append({
            "name": eventName,
            "place": eventPlace,
            "lat": eventLatitude,
            "lon": eventLongitude,
            "date": timestamp.isoformat()
        })

    except:
        print("error")
        latitudeArray.append(None)
        longitudeArray.append(None)
        continue





json_str_events = json.dumps(events, ensure_ascii=False)
print(json_str_events)
