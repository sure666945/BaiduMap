import requests
import json

ak = 'LAInFGSPGUSqRkOGENsDVclsc6a2eWq5'
url = 'https://api.map.baidu.com/directionlite/v1/transit'
origin = "39.99242,116.302269"
destination = "39.88066,116.388442"

def getjson(url, ak, origin, destination):
    pa = {
        'ak'          : ak,
        'origin'      : origin,
        'destination' : destination
    }
    r = requests.get(url, params=pa)
    decode_json = json.loads(r.text)
    return decode_json

# print(getjson(url, ak, origin, destination))

decode_json = getjson(url, ak, origin, destination)
print("status : ", decode_json['status'])
print("origin : ", decode_json['result']['origin'])
print("length = ", len(decode_json['result']['routes']))
for i in range(0, len(decode_json['result']['routes'])):
    print("======rout[", i, "]========")
    print("duration = ", decode_json['result']['routes'][i]['duration'])
    for step in decode_json['result']['routes'][i]['steps']:
        print(step[0]['instruction'])