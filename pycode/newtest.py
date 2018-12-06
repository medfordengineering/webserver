import urllib.request, json

url = "https://api.openweathermap.org/data/2.5/weather?q=Boston,us&appid=6879992ce17ac90aca1aebc85874b349"
response = urllib.request.urlopen(url).read()
data = json.loads(response.decode('utf-8'))

lst1 = []
lst2 = []

d2 = data['weather'][0]['main']
d1 = data['weather'][0]['description']
d3 = data['main']['temp']
lst1.append({'cond':d2, 'des':d1})

print(d3)
print(lst1)
'''

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
'''
    

