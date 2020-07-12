from django.shortcuts import render,redirect
from .forms import weatherform
from .serializer import EmbededSerializer
from django.conf import settings
import requests
import json
import pytz
from datetime import datetime
from timezonefinder import TimezoneFinder
from django.contrib import messages




def get_time_zone(longitude,latitute):
    tf=TimezoneFinder()
    time_zone=tf.timezone_at(lng=longitude,lat=latitute)
    return time_zone



def get_time_date(Time_zone):
    IST=pytz.timezone(Time_zone)
    datetime_IST=datetime.now(IST)
    get_date=datetime_IST.strftime('%d'" "'%B'" "'%A')
    get_time=datetime_IST.strftime('%I:%M %p')
    return get_date,get_time



def get_weather_photos(city_name,page_no):

    r3=requests.get('https://api.unsplash.com/search/collections?page='+page_no+'&query='+ city_name +'&client_id=VPYbAHkfJHrTcEOQxaw2SN0dDE6w81mLzzAKtKEELf4').json()
    
    preview_photos = [sub['preview_photos'] for sub in r3['results']] 
    url=[sub['urls'] for item  in preview_photos for sub in item ]
    thumb=[item['thumb'] for item in url]

    return thumb
    


def get_weather_data(city):
    
    r1=requests.get('http://api.openweathermap.org/data/2.5/weather?q=' +city+ '&appid='+settings.EMBEDLY_KEY+ '&units=metric').json()

    weather_data ={
                    'longitude':r1['coord']['lon'],
                    'latitude':r1['coord']['lat'],
                    'city':r1['name'],
                    'description':r1['weather'][0]['description'],
                    'icon':r1['weather'][0]['icon'],
                    'temp':int(r1['main']['temp']),
                    'feels_like':int(r1['main']['feels_like']),
                    'temp_min':int(r1['main']['temp_min']),
                    'temp_max':int(r1['main']['temp_max']),

                }


    return weather_data


def photo_range(photo_list,range_value):
    photo=[]
    for i in range(range_value):
        photo.append(photo_list[i])
     
    return photo





def home(request):
    try:
        photo=[]
        r2=requests.get('https://ipinfo.io').json()
        form=weatherform()
        city= r2['city']
        region= r2['region']
        global input_city
        input_city=city

        weather_data=get_weather_data(city)
       
        
        longitude=weather_data['longitude']
        latitude=weather_data['latitude']
        Time_zone=get_time_zone(longitude,latitude)
        date,time=get_time_date(Time_zone)

        thumb=get_weather_photos(input_city,'1')
         

        photo = photo_range(thumb,4)
        photos=photo_range(thumb,9)

        
        return render(request,'index.html',{'city':city,'region':region,'form':form,'weather_data':weather_data ,'date':date,'time':time,'photo':photo,'photos':photos})

    
    
    
    except KeyError:
        messages.info("could'nt find the temperture for this city")
        
        return render(request,'index.html')


def weatherdata(request):
    try:
        photo=[]
        if request.method =='POST':
            form=weatherform(request.POST)
            if form.is_valid():
                
                name=form.cleaned_data['name']
                
                weather_data=get_weather_data(name)
                
                global input_city
                input_city=weather_data['city']
                
                longitude=weather_data['longitude']
                latitude=weather_data['latitude']
                Time_zone=get_time_zone(longitude,latitude)
                date,time=get_time_date(Time_zone)
                
                thumb=get_weather_photos(input_city,'1')
                
                photo = photo_range(thumb,4)
                photos=photo_range(thumb,9)
                
                return render(request,'index.html',{'form':form,'weather_data':weather_data,'date':date,'time':time,'photo': photo,'photos':photos}) 
            

        else:
            form=weatherform()
        
        
        return render(request,'index.html',{'form':form}) 

    except KeyError:
        
        form=weatherform()
    
        messages.info(request,"could'nt find the temperture for this city")
        
        return render(request,'index.html',{'form':form})




def liveimages(request):
    try:
        if request.method=='POST':
            page_no =request.POST['page_no']

        else:
            page_no='1'
           
        
        
        thumb= get_weather_photos(input_city,page_no)


        
        return render(request,'live-cameras.html',{'thumb':thumb,'input_city':input_city,'page_no1':page_no})

    except (NameError,ValueError):
        return redirect("/")



def facebook(request):
    return redirect("www.facebook.com")


def twitter(request):
    return redirect("www.twitter.com")


def google(request):
    return redirect("www.google.com")
    

def pininterest(request):
    return redirect("www.pininterest.com")