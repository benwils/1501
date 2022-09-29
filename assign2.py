# help convert decimal to dms https://www.calculatorsoup.com/calculators/conversions/convert-decimal-degrees-to-degrees-minutes-seconds.php
#helped to figure out functions https://www.w3schools.com/python/python_functions.asp

import math
lat_1 = math.radians(51.098540670795096)
lat_2 = math.radians(51.013760)
long_1 = math.radians(114.18546544199816)
long_2 = math.radians(114.133691)
RADIUS_E = (6_378_137)
RADIUS_P = (6_356_752)
a = math.sin((lat_1 - lat_2)/2)**2 + math.cos(lat_1) * math.cos(lat_2) * math.sin((long_1 - long_2)/2)**2
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
R = (1/3) * (2 * RADIUS_E + RADIUS_P)
dist_m = R * c
dist_km = round((dist_m / 1000))
print(dist_km)
lat_1 = (51.098540670795096)
lat_2 = (51.013760)
long_1 = (114.18546544199816)
long_2 = (114.133691)
def decimal_to_dms(decimal):
    d = int(decimal)
    m = int((decimal - d) * 60)
    s = ((((decimal - d) ) * 60 )- m ) * 60
    print(d, m, s)
decimal_to_dms(lat_1)
decimal_to_dms(lat_2)
decimal_to_dms(long_1)
decimal_to_dms(long_2)



