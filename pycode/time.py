import urllib, json, time
from pytz import timezone
from datetime import datetime
from dateutil import parser

#test for git
asdfas 

#set time zone to eastern standard time
est = timezone('EST')

#get current time
current = datetime.now(est)

#convert current time to Unix timestamp in seconds
px = time.mktime(current.timetuple())
print px

#get JSON data
url = "https://api-v3.mbta.com/predictions?filter[stop]=9147&filter[route]=134&include=stop,trip"
response = urllib.urlopen(url)
data = json.loads(response.read())

#parse arrival time from JSON
d2 = data['data'][0]['attributes']['departure_time']

#convert arrival time unicode string into datetime object
d3 = parser.parse(d2)

#convert arrival tiem to Unix timestamp in seconds
dp = time.mktime(d3.timetuple())
print dp

#get difference in seconds and convert to minutes
print int(dp - px) /60

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
