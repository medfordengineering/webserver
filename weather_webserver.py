import urllib.request,json, time
from flask import Flask
from pytz import timezone
from datetime import datetime 
from dateutil import parser

app = Flask(__name__)

url = "https://api.openweathermap.org/data/2.5/weather?q=Boston,us&appid=6879992ce17ac90aca1aebc85874b349"

def time_diff(c_time):
    #set time zone to eastern standard time
    est = timezone('EST')
    #get current time
    now = datetime.now(est)
    #convert current time to Unix timestamp in seconds
    now_unix = time.mktime(now.timetuple())
    
    #convert arrival time unicode string into datetime object
    elapse_dt = parser.parse(c_time)
    #convert arrival time to Unix timestamp in seconds
    elapse_unix = time.mktime(elapse_dt.timetuple())
    #get difference in seconds and convert to minutes
    return int(elapse_unix - now_unix) / 60

def weather(data):

    weather = []

    base = data['weather'][0]['description']
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    wind = data['wind']['speed']

    weather.append({'general':base, 'temperature':temp, 'humidity':humidity, 'wind':wind})

    return (weather)

def get_arrival(data):

    times = []
    headsigns = []
    top = {}

    x = 0
    #Extract arrival_time and trip ID
    for e in data['data']:
        a_time = data['data'][x]['attributes']['departure_time']
        elapse_time = round(time_diff(a_time))
        trip_id = data['data'][x]['relationships']['trip']['data']['id']
        times.append({'id':trip_id, 'time':elapse_time})
        x = x + 1
        
    x = 0
    #Extract headsign and trip ID 
    for e in data['included']:
        trip_type = data['included'][x]['type']
        if trip_type == "trip":
            headsign = data['included'][x]['attributes']['headsign']
            trip_id = data['included'][x]['id']
            headsigns.append({'id':trip_id, 'headsign':headsign})
        x = x + 1

    #Link headsigns with arrival_times and trip ID
    for ta in times:
        for tb in headsigns:
            if ta['id'] == tb['id']:
                ta.update(tb)

    #Insert list into dictionary so that there is a root value in the JSON
    top['data'] = times

    #THIS IS IMPORTANT DO NOT PREPARSE THE JSON WITH DUMPS!!!
    #return json.dumps(top)
    return (top)
    
@app.route('/')
def display():
    #Get JSON from MBTA API
    contents = urllib.request.urlopen(url).read()
    j = json.loads(contents.decode('utf-8'))

    #j_parsed = get_arrival(j)
    j_parsed = weather(j)
    return json.dumps(j_parsed)  

    print(j_parsed)


if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
