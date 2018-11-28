
from flask import Flask
import urllib.request
import json
import datetime
app = Flask(__name__)

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
