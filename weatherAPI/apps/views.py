from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages
from apps.models import History
from .forms import HistoryModelForm
import json
import requests

# Create your views here.



def index(request):
    form = HistoryModelForm()
    weather_info = History.objects.all()
    #five_session = []


    if request.method == "POST" and 'action_one' in request.POST:
        form = HistoryModelForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data.get('city')

            '''if 'test_city' in request.COOKIES:
                return HttpResponse('Your lucky_number is {}'.format(request.COOKIES['test_city']))'''

            #rows = []
            url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=bd45fc9db8849cb46d00a451483ccd44'.format(city)
            r = requests.get(url)
            data = r.json()

            ## if input city did not exist
            if data['cod'] == '404':
                messages.error(request, 'Sorry, city not found.')

            ## store the weather_info into DB
            else:
                instance = form.save(commit=False)
                instance.temp = data['main']['temp']
                instance.maxtp = data['main']['temp_max']
                instance.mintp = data['main']['temp_min']
                instance.humidity = data['main']['humidity']
                instance.describ = data['weather'][0]['description']
                instance.save()
            #request.session.clear()

            ## calculate the session number
            num_visits = request.session.get('num_visits', 0)
            current_num = num_visits + 1
            request.session['num_visits'] = current_num
            request.session[str(current_num)] = city
            if current_num > 5 :
                del request.session[str(current_num - 5)]

            return redirect('index')

    five_session = []
    if 'num_visits' in request.session:
        now_num = request.session['num_visits']

        if now_num >5:
            for num in range(now_num-5, now_num):
                five_session.append(request.session.get(str(num)))
        else:
            for num in range(1,now_num+1):
                five_session.append(request.session.get(str(num)))
                print(request.session.get(str(num)))
    #print(five_session)

    context = {
        'form': form,
        'weather_info': weather_info,
        'five_session':five_session
    }

    return render(request, 'index.html', context=context)


