from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.template.context_processors import csrf
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from .models import URL_table
import urllib.request, urllib.error

# Create your views here.


def getResponseCode(url):
    try:
        conn = urllib.request.urlopen(url)
        return conn.getcode()
    except urllib.error.HTTPError:
        return 404
    except urllib.error.URLError:
        return 404
    except:
        return 404


def index(request):
    template_name = 'mainApp/1.html'
    args = {}

    if request.POST:
        if request.POST.get('URL', '') != '':
            URL_table(user_id=request.user.id, url=request.POST.get('URL', '')).save()

    if request.user.is_authenticated:
        args['user_url'] = [(i, getResponseCode(i.url)) for i in URL_table.objects.filter(user_id=request.user.id)]
        return render(request, template_name, args)
    else:
        return redirect('http://127.0.0.1:8000/login')


def login(request):
    template_name = 'mainApp/login.html'
    args = {}
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return redirect('http://127.0.0.1:8000')
            else:
                args['login_error'] = "Invalid user"
                return render(request, template_name, args)
        else:
            args['login_error'] = "Invalid"
            return render(request, template_name, args)
    else:
        return render(request, template_name)


def logout(request):
    auth.logout(request)
    return redirect('/')