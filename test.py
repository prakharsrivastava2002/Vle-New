from geopy.distance import geodesic as GD
import pandas as pd
import xlsxwriter
import sys

path_excel = r"D:\INTERNSHIP RELATED FILES\New Village details of Gazipur.xlsx"
df = pd.read_excel(path_excel)
radius = float(input("Enter the radius "))
Vle_coordinates = []
for i in range(2):
     Vle_coordinates.append(float(input("Enter the Latitude and Longitude")))

Village_Name = list(df["Village Name"])
Lats = list(df["Latitude"])
Longs = list(df["Longitude"])
Population = list(df['Village Population'])

temp = list(zip(Lats,Longs))
villages= dict((key,value) for key,value in zip(Village_Name,temp))
distance =[]

for key,values in villages.items():
    d = (GD(Vle_coordinates,values).km)
    distance.append(round(d,2))

Vle_details = list(zip(Village_Name,distance,Population))

s = sorted(Vle_details, key = lambda x: (x[1], -x[2]))



for items in s:
    if (items[1]<=radius):
        print(items[0])


#lst = list()
#for item in s:
 #   lst.append(item[0])

#var = int(input("Enter the No. of villages assigned per day"))
#output = [lst[i:i + var] for i in range(0,len(lst),var)]

#day = 1
#for item in output:
 #   print("Day "+ str(day)+ " : ", item)
  #  day = day+1




