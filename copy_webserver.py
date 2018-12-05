from flask import Flask
from pytz import timezone
from datetime import datetime
from dateutil import parser
import urllib, json, time

app = Flask(__name__)

def time_diff(c_time):
    
    #set time zone to eastern standard time
    est = timezone('EST')
    #get current time
    now = datetime.now(est)
    #convert current time to Unix timestamp in seconds
    now_unix = time.mktime(now.timetuple())

    #convert arrival time unicode string into datetime object
    elapse_dt = parser.parse(c_time)
    #convert arrival tiem to Unix timestamp in seconds
    elapse_unix = time.mktime(elapse_dt.timetuple())
    #get difference in seconds and convert to minutes
    return int(elapse_unix - now_unix) /60

#get JSON data
url = "https://api-v3.mbta.com/predictions?filter[stop]=9147&filter[route]=134&include=stop,trip"
response = urllib.urlopen(url)
data = json.loads(response.read())

#parse arrival time from JSON
temp_time = data['data'][0]['attributes']['departure_time']

temp_diff = time_diff(temp_time)
print temp_diff


url = "https://api-v3.mbta.com/predictions?filter[stop]=9147&filter[route]=134&include=stop,trip"

def nicify(j):
    r = {} # return obj
    h = {} # headsign dict

    for t in j["included"]:
        if t["type"] == "trip":
            h[t["id"]] = t["attributes"]["headsign"]
            r[h[t["id"]]] = []
    print(h)
    for p in j["data"]:
        tm = p["attributes"]["arrival_time"]
        hs = h[p["relationships"]["trip"]["data"]["id"]]
        
    #    r[hs].append(int(tm[14:16]) * 60 + int(tm[17:19]))
    #print(r)
    #return json.dumps(r)
    return json.dumps(hs)
@app.route('/')
def display():
    contents = urllib.request.urlopen(url).read()
    j = json.loads(contents.decode('utf-8'))
    r = nicify(j)
    return r
if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
