# calculate the duration of the year on the planets
from math import pi
r=input("Enter the radius of the orbits(million km:) ->")
v=input("Enter the speed(km/s) ->")
r=float(r)
v=float(v)
r=r*1000000
year=2*pi*r/v
print(year)
year=year/(60*60*24)
print(round(year))