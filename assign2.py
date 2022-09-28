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
print(a)
print(c)
print("R",R)
print(dist_m)
print(dist_km)