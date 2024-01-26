import  requests
from django.core.cache import cache
from django.shortcuts import render
from django.views.generic import View
from techtest.utils import json_response
from .forms import GetTemperatureInfo

class WeatherListView(View):

    def get(self,response):

        form = GetTemperatureInfo()
        return render(response, "main/main.html", {"form":form})


    def post(self, response):
        
        # Getting the data from  the form
        response = response.POST
        city_name = response["city_name"]        
        language = response["lang"]

        # looking up the data in cache, cache is set to delete after 10 minutes
        if cache.get(f"{city_name}{language}"):
            response = cache.get(f"{city_name}{language}")
            data = response
            
        else:
                
            url = "https://api.openweathermap.org/data/2.5/weather?q="
            api_key = "186316716709c31e9f17840d653a9eba"
            
            #Calling the API with proper data

            try:
                response =  requests.get(f"{url}{city_name}&lang={language}&units=metric&appid={api_key}")
                            
                
            except requests.ConnectionError:
                return json_response(data ={"message": "Resource Unavailable "}, status= 400)
            
            if response.status_code != 200:
                return json_response(data =response.json(), status= response.status_code)   
            
            # refining the API data

            response= response.json()
            data ={}
            data["city"] = city_name
            data["temperature"] = response["main"]
            data["wind"] = response["wind"]
            data["description"] =  response["weather"][0]["description"]

            # Making entry to cache
            cache.set(f"{city_name}{language}", data, timeout=600)
            
            
        return json_response(data)
        
      


