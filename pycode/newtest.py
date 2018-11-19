import urllib, json

url = "https://api-v3.mbta.com/schedules?filter[route]=94&filter[stop]=15002&include=prediction,stop,trip"
response = urllib.urlopen(url)
data = json.loads(response.read())

lst1 = []
lst2 = []

for x in range(10):
    d2 = data['data'][x]['attributes']['arrival_time']
    d1 = data['data'][x]['relationships']['trip']['data']['id']
    lst1.append({'id':d2, 'time':d1})

for elem in lst1:
    print elem['id'], elem['time']

for x in range(10):
    d2 = data['included'][x+1]['attributes']['headsign']
    d1 = data['included'][x+1]['id']
    lst2.append({'id':d1, 'headsign':d2})

for elem in lst2:
    print elem['id'], elem['headsign']

for ta in lst1: 
    for tb in lst2:
        if ta['id'] == tb['id']:
            ta.update(tb)

for i in lst1:
    print i['id']
    print i['headsign']
    print i['time']

