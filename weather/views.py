from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
# Create your views here.


def home(request):
    return render(request, 'home.html')


def get_weather(request):
    city = request.GET['place']
    
    try:

        data = requests.get(
            f'https://www.google.com/search?q={city}+weather&oq={city}+w&aqs=chrome.1.69i57j0l9.3942j0j7&sourceid=chrome&ie=UTF-8')

        soup = BeautifulSoup(data.content, 'html5lib')

        place1 = soup.find('span', class_='BNeawe tAd8D AP7Wnd')

        temperature = soup.find('div', class_='BNeawe iBp4i AP7Wnd')

        Datetime = soup.find('div', class_='BNeawe tAd8D AP7Wnd')

        status = "Success"

        context_data = {'place': place1.text,
                        'temperature': temperature.text[0:2], 'time': Datetime.text, 'status': status}

    except:
        print("error occured")
        context_data = {'status': 'Not found'}

    return render(request, 'home.html', {'result': context_data})
