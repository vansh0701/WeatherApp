# import pytz
# from datetime import datetime
# from timezonefinder import TimezoneFinder

# tf = TimezoneFinder()
# latitude, longitude = 28.67 , 77.22
# Time_zone=tf.timezone_at(lng=longitude, lat=latitude) # returns 'Europe/Berlin'
# print(Time_zone)

# # UTC = pytz.utc
# IST = pytz.timezone(Time_zone)

# # print("UTC in Default Format : ",  
# #       datetime.now(UTC)) 
  
# datetime_ist=datetime.now(IST)

# print("IST in Default Format : ", datetime_ist.strftime('%H:%M:%S %Z %z') ) 
# print("IST in Default Format : ", datetime_ist.strftime( '%d' " " '%B' " " '%A'" "'%Y') ) 

import requests

r3=requests.get('https://api.unsplash.com/search/collections?page=1&query=newdelhi&client_id=VPYbAHkfJHrTcEOQxaw2SN0dDE6w81mLzzAKtKEELf4').json()
# print(r3)

            

res = [sub['preview_photos'] for sub in r3['results']] 
# print(res)

url=[sub['urls'] for item  in res  for sub in item ]

thumb=[item['thumb'] for item in url]

print(thumb)
