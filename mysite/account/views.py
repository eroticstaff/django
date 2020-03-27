from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.http import HttpResponse
# Create your views here.
def index(request):
    context={}
    return render(request, 'account/index.html', context)

def login(request):
    user = authenticate(username=request.POST.get('login'), password=request.POST.get('password'))
    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        return redirect('/account/')
