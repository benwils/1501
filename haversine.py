#USERNAME1: benwils
#USERNAME2: deckunai (collaborated togethere)
#help convert decimal to dms https://www.calculatorsoup.com/calculators/conversions/convert-decimal-degrees-to-degrees-minutes-seconds.php
#helped to figure out functions https://www.w3schools.com/python/python_functions.asp
#latitude and longtitude for location my house: 51.098540670795096, 114.18546544199816

import math
lat_1_deg = float(input("Enter latitude in decimal degrees: "))
long_1_deg = float(input("Enter longtitude in decimal degrees: "))
lat_1_rad = math.radians(lat_1_deg)
long_1_rad = math.radians(long_1_deg)
lat_2_deg = (51.013760)
long_2_deg = (114.133691)
lat_2_rad = math.radians(lat_2_deg)
long_2_rad = math.radians(long_2_deg)
RADIUS_E = (6_378_137)
RADIUS_P = (6_356_752)
a = (math.sin((lat_1_rad - lat_2_rad)/2)**2 + math.cos(lat_1_rad) * math.cos(lat_2_rad) * math.sin((long_1_rad - long_2_rad)/2)**2) 
c = 2 * math.atan2(math.sqrt(a),math.sqrt(1-a)) 
R = ((1/3) * (2 * RADIUS_E + RADIUS_P)) 
dist_km = round((R * c)/1000)
print(f"{dist_km:.1f}",'km')
def decimal_to_dms_N(decimal):
    d = int(decimal)
    m = int((decimal - d) * 60)
    s = (((((decimal - d)) * 60) - m) * 60)
    print((d),"º",(m),"'",f"{s:.2f}",'"',"N", sep = "")
def decimal_to_dms_W(decimal):
    d = int(decimal)
    m = int((decimal - d) * 60)
    s = (((((decimal - d)) * 60) - m) * 60)
    print((d),"º",(m),"'",f"{s:.2f}",'"',"W", sep = "")
decimal_to_dms_N(lat_1_deg)
decimal_to_dms_W(long_1_deg)
decimal_to_dms_N(lat_2_deg)
decimal_to_dms_W(long_2_deg)