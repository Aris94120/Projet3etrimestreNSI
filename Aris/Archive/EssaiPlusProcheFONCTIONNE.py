from math import cos, asin, sqrt

def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p)*cos(lat2*p) * (1-cos((lon2-lon1)*p)) / 2
    return 12742 * asin(sqrt(a))

def closest(data, v):
    return min(data, key=lambda p: distance(v['lat'],v['lon'],p['lat'],p['lon']))

tempDataList = [{'lat': 48.852108, 'lon': 2.468225},
                {'lat': 48.906241,  'lon': 2.404972 },
                {'lat': 48.899431, 'lon': 2.242910},
                {'lat': 48.330912, 'lon': 2.162082}]

v = {'lat': 48.8537499, 'lon': 2.4557951}
print(closest(tempDataList, v))
