from django.forms import model_to_dict
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from user.models import User

def join(request):
    user = User();
    user.email = request.POST['email']
    user.password = request.POST['password']
    user.name = request.POST['name']
    user.gender = request.POST['gender']

    user.save()

    return HttpResponseRedirect('/user/joinsuccess')

def joinsuccess(request):
    return render(request, 'user/joinsuccess.html')

def joinform(request):
    return render(request, 'user/joinform.html')


def login(request):
    result = User.objects.filter(email=request.POST['email']).filter(password=request.POST['password'])
    if len(result) == 0:
        return HttpResponseRedirect('/user/loginform?result=false')
    authuser = result[0]
    request.session['authuser'] = model_to_dict(authuser)
    # return HttpResponse(authuser)
    return HttpResponseRedirect('/')

def logout(request):
    del request.session['authuser']
    return HttpResponseRedirect('/')

def loginform(request):
    return render(request, 'user/loginform.html')

