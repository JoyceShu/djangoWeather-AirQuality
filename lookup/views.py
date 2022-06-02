from django.shortcuts import render

# Create your views here.
#https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=95132&distance=100&API_KEY=0DC09709-3FB4-488E-BA7F-EB82F87C9347
def home(request):
    import json
    import requests
    
    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=100&API_KEY=0DC09709-3FB4-488E-BA7F-EB82F87C9347")
        try:
            api = json.loads(api_request.content)
        
        except Exception as e:
            api = "Error..."
        
        if api[0]['Category']['Name'] == "Good":
            category_description  = "(0-50) Air quality is considered satisfactory."
            category_color = "good"

        elif api[0]['Category']['Name'] == "Moderate":
            category_description  = "(51-100) Air quality is acceptable."
            category_color = "moderate"

        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_color = "usg"
            category_description  = "(101-105) Generally public is not likely to be affected at this AQI."

        elif api[0]['Category']['Name'] == "Unhealthy" :
            category_color = "unhealthy"
            category_description  = "(151-200) Everyone may begin to experience health effects."

        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_color = "veryunhealthy"
            category_description  = "(201-300) Health alert: everyone may experience more serious health effects."

        elif api[0]['Category']['Name'] == "Hazardous":
            category_color = "hazardous"
            category_description  = "(301-500) Health warning of emergency conditions."
        
        return render(request, 'home.html', {'api':api, 'category_color':category_color, 'category_description':category_description})
            
        

    else:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=95132&distance=100&API_KEY=0DC09709-3FB4-488E-BA7F-EB82F87C9347")
        try:
            api = json.loads(api_request.content)
        
        except Exception as e:
            api = "Error..."
        
        if api[0]['Category']['Name'] == "Good":
            category_description  = "(0-50) Air quality is considered satisfactory."
            category_color = "good"

        elif api[0]['Category']['Name'] == "Moderate":
            category_description  = "(51-100) Air quality is acceptable."
            category_color = "moderate"

        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_color = "usg"
            category_description  = "(101-105) Generally public is not likely to be affected at this AQI."

        elif api[0]['Category']['Name'] == "Unhealthy" :
            category_color = "unhealthy"
            category_description  = "(151-200) Everyone may begin to experience health effects."

        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_color = "veryunhealthy"
            category_description  = "(201-300) Health alert: everyone may experience more serious health effects."

        elif api[0]['Category']['Name'] == "Hazardous":
            category_color = "hazardous"
            category_description  = "(301-500) Health warning of emergency conditions."
        
        return render(request, 'home.html', {'api':api, 'category_color':category_color, 'category_description':category_description})
            
        

        

def about(request):
    return render(request, 'about.html', {})