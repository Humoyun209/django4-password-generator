from django.shortcuts import render
import random
from string import ascii_lowercase, digits, punctuation, ascii_uppercase


def index(request):
    rang = list(range(1, 21))
    context = {
        'rang': rang
    }
    return render(request, 'generator/index.html', context)


def show_password(request):
    stringpass = ascii_lowercase
    password = []
    length = int(request.GET.get('length'))
    if request.GET.get('upper'):
        stringpass += ascii_uppercase
    if request.GET.get('digits'):
        stringpass += digits
    if request.GET.get('character'):
        stringpass += '><\/?!@#'
    for i in range(1, length+1):
        password.append(random.choice(list(stringpass)))
    password = ''.join(password)

    context = {
        'password': password,
    }
    print(request.GET.get('upper'))
    return render(request, 'generator/show_pass.html', context)