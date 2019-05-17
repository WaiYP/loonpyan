from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    # if not request.user.is_authenticated():
    return render(request, 'administration/login.html')
    # else:
    #     return render(request, 'administration/index.html', {})

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'administration/index.html', {})
            else:
                return render(request, 'administration/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'administration/login.html', {'error_message': 'Invalid login'})
    return render(request, 'administration/login.html')


def user_logout(request):
    logout(request)
    return render(request, 'administration/login.html')
