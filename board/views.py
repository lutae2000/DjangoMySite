from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Board

# Create your views here.
def index(request):
    kwd = request.GET.get('kwd')
    if kwd is not None:
        board_list = Board.objects.filter(title__icontains=kwd).order_by('-id')
    else:
        board_list = Board.objects.filter().order_by('-id')
    page = request.GET.get('page', 1)

    paginator = Paginator(board_list, 5)
    try:
        board_list = paginator.page(page)
    except PageNotAnInteger:
        board_list = paginator.page(1)
    except EmptyPage:
        board_list = paginator.page(paginator.num_pages)
    return render(request, 'board/list.html', {'board_list': board_list, 'kwd':kwd})

def view(request):
    board = Board()
    board.id = request.POST.get('id', request.GET.get('id'))
    instance = Board.objects.filter(id=board.id).get()
    Board.objects.filter(id=board.id).update(count=instance.count+1)
    context = {'board' : instance }
    return render(request, 'board/view.html', context)

def modify(request):
    if request.POST.get('id') is not None :
        board = Board()
        board.id = request.POST.get('id')

        board.title = request.POST['title']
        board.contents = request.POST['contents']
        Board.objects.filter(id=board.id).update(title=board.title, contents=board.contents)


    return HttpResponseRedirect('/board')

def modifyform(request):
    board = Board()
    board.id = request.POST.get('id', request.GET.get('id'))
    instance = Board.objects.filter(id=board.id).get()
    print("instance:", instance)
    context = {'board' : instance}
    return render(request, 'board/modify.html', context)

def write(request):
    if request.POST.get('user_id', request.GET.get('user_id')) is not None :
        board = Board()
        board.name = request.POST['name']
        board.title = request.POST['title']
        board.contents = request.POST['contents']
        board.user_id = request.POST['user_id']

        board.save()

    return HttpResponseRedirect('/board')

def writeform(request):
    if request.POST.get('id', request.GET.get('id')) == '' :
        return HttpResponseRedirect('/user/loginform')

    context = {'boardName' : request.session['authuser']['name'], 'boardUser_id' : request.session['authuser']['id']}
    return render(request, 'board/write.html', context)


def delete(request):
    board = Board()
    board.id = request.POST.get('id', request.GET.get('id'))
    instance = Board.objects.filter(id=board.id).get()
    instance.delete()

    return HttpResponseRedirect('/board')

