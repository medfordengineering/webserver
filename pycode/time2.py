import urllib, json, time
from pytz import timezone
from datetime import datetime
from dateutil import parser

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

"""
print (
#print current.day
#print (current.hour - 12)
#print current.minute


import urllib, json, datetime
from pytz import timezone

#url = "https://api-v3.mbta.com/schedules?filter[min_time]=2:15&filter[max_time]=14:30&filter[stop]=9147&include=prediction,stop,trip"
url = "https://api-v3.mbta.com/predictions?filter[stop]=9147&filter[route]=134&include=stop,trip"
response = urllib.urlopen(url)
data = json.loads(response.read())

lst1 = []
lst2 = []

x = 0

for e in data['data']:
#    d2 = data['data'][x]['attributes']['arrival_time']
    d2 = data['data'][x]['attributes']['departure_time']
    d1 = data['data'][x]['relationships']['trip']['data']['id']
    lst1.append({'id':d1, 'time':d2})
    x = x + 1
for elem in lst1:
    print elem['id'], elem['time']
x = 0;
for e in data['included']:
    d3 = data['included'][x]['type']
    if d3 == "trip":
        d2 = data['included'][x]['attributes']['headsign']
        d1 = data['included'][x]['id']
        lst2.append({'id':d1, 'headsign':d2})
        x = x + 1
for elem in lst2:
    print elem['id'], elem['headsign']

for ta in lst1: 
    for tb in lst2:
        if ta['id'] == tb['id']:
            ta.update(tb)
for i in lst1:
    i['hrs'] = i['time'][11:13]
    i['min'] = i['time'][14:16]

for i in lst1:
    print i['id'],
    print i['headsign'],
    print i['time'],
    print i['hrs'],
    print i['min']
#days, hrs, mins, secs = d4.split(':') 

#d4 = lst1[0]['time']

#print d4[1:5]
print d4
days, hrs, mins, secs = d4.split(':') 
print hrs
print mins
print secs
"""
