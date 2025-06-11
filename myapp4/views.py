from django.shortcuts import render
import requests
import datetime

# Create your views here.
def home(request):
    weather=None
    value=None
    if request.method=="POST":
        city=request.POST.get("city")
        api='2c2c497bb613f24a5b3137f328e6eaf7'
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric"
        res=requests.get(url) 
        data=res.json()
        if data.get("cod")==200:
            weather={
            'city':city, 
            'temp':data['main']['temp'],
            'icon':data['weather'][0]['icon'],
            'discription':data['weather'][0]['description'],
            'time':datetime.date.today(),
            }
            return render(request,"home.html",{"weather":weather})
        else:
            error="city not found"
            return render(request,"home.html",{'error':error}) 
    return render(request,"home.html",{'weather':weather}) 
    

 

 

 