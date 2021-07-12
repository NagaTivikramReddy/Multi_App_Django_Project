from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from . import models

import os
import requests


def home(request):
    return render(request, 'currencyconvertor/home.html')


def convert(request):
    amount = int(request.GET['amount'])
    from1 = request.GET['fromcountries']
    to = request.GET['tocountries']

    EXCHANGERATES_API_KEY = os.environ.get('EXCHANGERATES_API_KEY')
    url = f'http://api.exchangeratesapi.io/v1/latest?access_key={EXCHANGERATES_API_KEY}'

    response = requests.get(url)
    data = response.json()

    EUR = 1
    INR = data['rates']['INR']
    USD = data['rates']['USD']
    KWD = data['rates']['KWD']
    EGP = data['rates']['EGP']
    JPY = data['rates']['JPY']

    if from1 == 'eur' and to == 'eur':
        result = amount

    elif from1 == 'eur' and to == 'inr':
        result = (INR/EUR)*amount
    elif from1 == 'inr' and to == 'eur':
        result = (EUR/INR)*amount

    elif from1 == 'eur' and to == 'usd':
        result = (USD/EUR)*amount
    elif from1 == 'usd' and to == 'eur':
        result = (EUR/USD)*amount

    elif from1 == 'eur' and to == 'jpy':
        result = (JPY/EUR)*amount
    elif from1 == 'jpy' and to == 'eur':
        result = (EUR/JPY)*amount

    elif from1 == 'egp' and to == 'eur':
        result = (EUR/EGP)*amount
    elif from1 == 'eur' and to == 'egp':
        result = (EGP/EUR)*amount

    elif from1 == 'eur' and to == 'dinar':
        result = (KWD/EUR)*amount
    elif from1 == 'dinar' and to == 'eur':
        result = (EUR/KWD)*amount

    # --------------------------
    elif from1 == 'inr' and to == 'inr':
        result = amount

    elif from1 == 'inr' and to == 'usd':
        result = (USD/INR)*amount
    elif from1 == 'usd' and to == 'inr':
        result = (INR/USD)*amount

    elif from1 == 'inr' and to == 'egp':
        result = (EGP/INR)*amount
    elif from1 == 'egp' and to == 'inr':
        result = (INR/EGP)*amount

    elif from1 == 'inr' and to == 'dinar':
        result = (KWD/INR)*amount
    elif from1 == 'dinar' and to == 'inr':
        result = (INR/KWD)*amount

    elif from1 == 'inr' and to == 'jpy':
        result = (JPY/INR)*amount
    elif from1 == 'jpy' and to == 'inr':
        result = (INR/JPY)*amount

    elif from1 == 'usd' and to == 'usd':
        result = amount

    elif from1 == 'usd' and to == 'egp':
        result = (EGP/USD)*amount
    elif from1 == 'egp' and to == 'usd':
        result = (USD/EGP)*amount

    elif from1 == 'usd' and to == 'jpy':
        result = (JPY/USD)*amount
    elif from1 == 'jpy' and to == 'usd':
        result = (USD/JPY)*amount

    elif from1 == 'usd' and to == 'dinar':
        result = (KWD/USD)*amount
    elif from1 == 'dinar' and to == 'usd':
        result = (USD/KWD)*amount

    elif from1 == 'egp' and to == 'egp':
        result = amount

    elif from1 == 'egp' and to == 'jpy':
        result = (JPY/EGP)*amount
    elif from1 == 'jpy' and to == 'egp':
        result = (EGP/JPY)*amount

    elif from1 == 'egp' and to == 'dinar':
        result = (KWD/EGP)*amount
    elif from1 == 'dinar' and to == 'egp':
        result = (EGP/KWD)*amount

    elif from1 == 'jpy' and to == 'jpy':
        result = amount

    elif from1 == 'jpy' and to == 'dinar':
        result = (KWD/JPY)*amount

    elif from1 == 'dinar' and to == 'jpy':
        result = (JPY/KWD)*amount

    else:
        result = None

    equal = '='

    return render(request, 'currencyconvertor/home.html', {'result': result, 'amount': amount, 'from': from1, 'to': to, 'equal': equal})


def newconvert(request):

    # print(f'INR {INR}, USD {USD}, KWD {KWD}, EGP {EGP},JPY {JPY}')

    # amount = int(request.GET['amount'])
    # from1 = request.GET['fromcountries']
    # to = request.GET['tocountries']

    # temp = "INR : 88.453891 USD : 1.1875 JPY : 130.808992 EGP : 18.603597 KWD : 0.357449 RUB : 88.255163"

    EUR = 1

    INR = 88.453891
    USD = 1.1875
    JPY = 130.808992
    EGP = 18.603597
    KWD = 0.357449
    # RUB = 88.255163

    equal = '='

    # return render(request, 'currencyconvertor/home.html', {'result': result, 'amount': amount, 'from': from1, 'to': to, 'equal': equal})

    return render(request, 'currencyconvertor/newhome.html')
