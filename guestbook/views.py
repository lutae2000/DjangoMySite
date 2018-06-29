from django.shortcuts import render
from .models import Guestbook
from django.http import HttpResponseRedirect
from django.contrib import messages


# Create your views here.
def index(request):
    guestbook_list = Guestbook.objects.all().order_by('-regdate')
    context = {'guestbook_list' : guestbook_list}
    return render(request, 'guestbook/list.html', context)


def add(request):
    guestbook = Guestbook()
    guestbook.name = request.POST['name']
    guestbook.password = request.POST['password']
    guestbook.message = request.POST['message']

    # DB에 저장
    guestbook.save()

    # 응답
    messages.info(request, 'Your Post has been uploaded successfully!')
    return HttpResponseRedirect('/guestbook')

def delete(request):
    guestbook = Guestbook()
    # GET 방식 처리방법...
    # https://github.com/tschellenbach/Django-facebook/pull/564/commits/32f5a0c13add2e2699becbe1459bab803ff313f2
    # 기존 >> print("request.REQUEST.get('name'): ", request.REQUEST.get('name'))
    # 최신 >> print("request.POST.get('name', request.GET.get('name')): ", request.POST.get('name', request.GET.get('name')))
    guestbook.name = request.POST.get('name', request.GET.get('name'))
    guestbook.regdate = request.POST.get('regdate')
    guestbook.password = request.POST.get('password')

    # objects 에 필터를 적용 할 수 있다.
    instance = Guestbook.objects.filter(name=guestbook.name).filter(password=guestbook.password)#.filter(regdate=request.POST['regdate'])
    if len(instance) == 0:
        print("비밀번호가 일치하지 않습니다.")
        return HttpResponseRedirect('/user/loginform?result=false')
    else:
        instance.delete()

    guestbook_list = Guestbook.objects.all().order_by('-regdate')
    context = {'guestbook_list' : guestbook_list}
    return render(request, 'guestbook/list.html', context)

def deleteform(request):
    guestbookName = request.POST.get('name', request.GET.get('name'))
    guestbookRegdate = request.POST.get('regdate', request.GET.get('regdate'))
    context = {'guestbookName' : guestbookName, 'guestbookRegdate' : guestbookRegdate }
    return render(request, 'guestbook/deleteform.html', context)
