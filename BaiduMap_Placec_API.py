from os import link
import requests
import json

ak  = 'LAInFGSPGUSqRkOGENsDVclsc6a2eWq5'
url = 'https://api.map.baidu.com/place/v2/search'
loc = '北京'

def getjson(url, loc, ak, page_num = 0):
    pa = {
        'query'     : '水岸桃源露营基地',
        'region'    : loc,
        'output'    : 'json',
        'scope'     : '2',
        'page_size' : 10,
        'ak'        : ak
    }
    r = requests.get(url, params=pa)
    decode_json = json.loads(r.text)
    return decode_json

print(getjson(url, loc, ak))
decode_json = getjson(url, loc, ak)
lat = decode_json['results'][0]['location']['lat']
lng = decode_json['results'][0]['location']['lng']
print('lat = ', lat)
print('lng = ', lng)