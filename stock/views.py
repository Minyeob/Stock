from django.shortcuts import render
from django.views.generic.base import TemplateView
import urllib.request
from stock.forms import *
from yahoo_finance import Share
# Create your views here.

def index(request):
    form=SearchForm()
    return render(request, 'counter/Theme/main.html', {'form':form})

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)

        #form이 유효한지 확인이 되지 않으면 form안의 데이터를 처리할 수 없도록 되어있다. 폼을 사용하기 위해서는 is_valid를 통해 유효성 확인후 폼의 데이터 사용
        if form.is_valid():
            code=form.cleaned_data['name']
            name=code+'.KS'
            avg_50day=Share(name).get_50day_moving_avg()
            current_price=Share(name).get_price()
            historical_price=Share(name).get_historical('2017-01-01', '2017-08-17')
            return render(request, 'counter/Theme/result.html', {'avg_50day': avg_50day, 'current_price':current_price, 'historical_price':historical_price})

    return render(request, 'counter/Theme/main.html')