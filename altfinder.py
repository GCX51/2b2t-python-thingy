import json
import http.client
import time
from datetime import datetime, timezone

conn = http.client.HTTPSConnection("api.2b2t.vc")
headers = {
    "User-Agent": "Python http.client",
    "Connection": "keep-alive"
}
data = "fuck you"
def get(param):
    global conn
    global data
    attempts = 0
    data = "html"
    while "html" in str(data):
        conn.request("GET", param, headers=headers)
        response = conn.getresponse()
        data = response.read()
        time.sleep(3)
    data = json.loads(data)
    trieslasttime=attempts

from datetime import datetime

PlayerA=input("whats player one?")
PlayerB=input("whats player two?")

get("/connections?pageSize=100&playerName="+PlayerA)
Apages = data["pageCount"]
Alist = [entry["time"] for entry in data["connections"]]
for i in range(1, Apages+1):
    get("/connections?pageSize=100&playerName="+PlayerA+"&page="+str(i))
    Alist = Alist+[entry["time"] for entry in data["connections"]]
    print(round(100*(i/Apages)),"% of data collected for", PlayerA)
Alist=[datetime.fromisoformat(i).timestamp() for i in Alist]
    
get("/connections?pageSize=100&playerName="+PlayerB)
Bpages = data["pageCount"]
Blist = [entry["time"] for entry in data["connections"]]
for i in range(1, Bpages+1):
    get("/connections?pageSize=100&playerName="+PlayerB+"&page="+str(i))
    Blist = Blist+[entry["time"] for entry in data["connections"]]
    print(round(100*(i/Bpages)),"% of data collected for", PlayerB)
Blist=[datetime.fromisoformat(i).timestamp() for i in Blist]

range_limit = 50
count = 0
for a in Alist:
    for b in Blist:
        if abs(a - b) <= range_limit:
            count += 1
print(count, "matches, from")
range_limit = 43200
count2 = 0
for a in Alist:
    for b in Blist:
        if abs(a - b) <= range_limit:
            count2 += 1
print(round(count2/864), "expected matches.")
print(round(100*count/(count2/864)), "%")
