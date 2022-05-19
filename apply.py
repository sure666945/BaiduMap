import requests
import json
import pandas as pd

ak  = 'LAInFGSPGUSqRkOGENsDVclsc6a2eWq5'
place_url = 'https://api.map.baidu.com/place/v2/search'
route_url = 'https://api.map.baidu.com/directionlite/v1/transit'
loc = '北京'
origin = "望京西园四区"

def place_search(url, ak, loc, destination, page_num = 0):
    pa = {
        'query'     : destination,
        'region'    : loc,
        'output'    : 'json',
        'scope'     : '2',
        'page_size' : 10,
        'ak'        : ak
    }
    r = requests.get(url, params=pa)
    place_json = json.loads(r.text)
    lat = place_json['results'][0]['location']['lat']
    lng = place_json['results'][0]['location']['lng']
    coord = str(lat) + ',' + str(lng)
    return coord

def route_search(url, ak, origin, destination):
    pa = {
        'ak'          : ak,
        'origin'      : origin,
        'destination' : destination
    }
    r = requests.get(url, params=pa)
    decode_json = json.loads(r.text)
    duration = decode_json['result']['routes'][0]['duration']
    return duration

if __name__ == "__main__":
    print('progtam start...')
    df = pd.read_excel(r'北京营地汇总.xlsx', header=None)
    origin_coord = place_search(place_url, ak, loc, origin)
    print('origin: ',origin, origin_coord)
    for i in range(1, (len(df.index - 1))):
        destination = df[2][i]
        destination_coord = place_search(place_url, ak, loc, destination)
        print("destination[", i, "]: ",destination, destination_coord)
        duration = route_search(route_url, ak, origin_coord, destination_coord)
        second = duration % 60
        minute = duration // 60 % 60
        hour   = duration // 60 // 60
        time = str(hour) + ' h ' + str(minute) + ' min ' + str(second) + ' s '
        print(time)
        df[8][i] = time
        df.to_excel('路线.xlsx', index = False, header = None)

