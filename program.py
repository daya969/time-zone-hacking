import requests
import json
import asyncio
import websockets


SERVER_WS = "ws://192.168.1.53:8765"


def get_ip_info():
  r = requests.get("https://ipinfo.io/json",timeout=5)
  return r.json()
def is_turk(info):
    return info.get(country) == "TR"


async def send(datainfo):
    asaync with websockets.connect(SERVER_WS) as ws:
         await ws.send(json.dumps(datainfo))



def main():
     info = get_ip_info()

if not is_turk(info):
   print('Error uses not in turkey')
   return # stop
lat, lot = map(float,info["loc"].split(","))
datainfo = {
    "country":"TR",
  "city":info.get("city")
  "org": info.get("org"),
  "lat":lat,
  "lon":lon
}

asayncio.run(send(datainfo))
print("[+] sended")
  
if __name__ =="__main__"
    main()
