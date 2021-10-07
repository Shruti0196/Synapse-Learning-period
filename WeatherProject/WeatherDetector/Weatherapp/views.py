from django.http.response import HttpResponse
from django.shortcuts import render,redirect
import json
import requests
from django.contrib import messages

def index(request):
    return render(request,'index.html')
    
def weather(request):
    if request.method=='POST':   
        city=request.POST['city']
        res=requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=4682b9a8567709871ff3f2d08899941e')
        if res:
            json_data=json.loads(res.text)
            try:
                cc=str(json_data['sys']['country'])
            except:
                cc="Not available" 
            try:
                coord=str(json_data['coord']['lon'])+'  '+str(json_data['coord']['lat'])
            except:
                coord="Not available"
            try:
                tempe=str(json_data['main']['temp'])+'K'
            except:
                tempe="Not available"
            try:
                pre=json_data['main']['pressure']
            except:
                pre="Not available"
            try:
                hum=json_data['main']['humidity']
            except:
                hum="Not available"

            data={
                "country_code":cc,
                "coordinate":coord,
                "temp":tempe,
                "pressure":pre,
                "humidity":hum
                }
        else:
            messages.info(request,'Enter correct country')
            return redirect('/')
    return render(request,'weather.html',{'data':data,'city':city})
    