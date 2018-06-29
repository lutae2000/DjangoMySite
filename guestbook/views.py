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
    guestbook.password = request.POST.get('password')

    print(guestbook)
    # objects 에 필터를 적용 할 수 있다.
    # print(Guestbook.objects.filter(name=request).delete())
    instance = Guestbook.objects.filter(name=guestbook.name).get()
    print("instance.password:", instance.password)
    if guestbook.password == instance.password :
        instance.delete()
        messages.info(request, 'Your Post has been deleted successfully!')
        print("Delete Complete!")
    else :
        messages.info(request, 'Passwords do not match!')
        print("비밀번호가 일치하지 않습니다.")

    guestbook_list = Guestbook.objects.all().order_by('-regdate')
    context = {'guestbook_list' : guestbook_list}
    return render(request, 'guestbook/list.html', context)

def deleteform(request):
    guestbook_name = request.POST.get('name', request.GET.get('name'))
    context = {'guestbook_name' : guestbook_name }
    return render(request, 'guestbook/deleteform.html', context)
