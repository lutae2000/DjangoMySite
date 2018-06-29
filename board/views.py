from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Board

# Create your views here.
def index(request):
    board = Board.objects.all().order_by('-id')
    data = {'board_list': board}
    return render(request, 'board/list.html', data)

def view(request):
    board = Board()
    board.id = request.POST.get('id', request.GET.get('id'))
    instance = Board.objects.filter(id=board.id).get()
    print("instance:", instance)
    context = {'board' : instance}
    return render(request, 'board/view.html', context)

def modify(request):
    if request.POST.get('id') is not None :
        board = Board()
        board.id = request.POST.get('id')

        print("boardid: ",board.id)
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
    if request.POST.get('name') is not None :
        board = Board()
        board.name = request.POST['name']
        board.title = request.POST['title']
        board.contents = request.POST['contents']
        board.user_id = request.POST['user_id']

        board.save()

    return HttpResponseRedirect('/board')

def writeform(request):
    if request.session['authuser'] is None :
        return HttpResponseRedirect('/user/loginform')

    context = {'boardName' : request.session['authuser']['name'], 'boardUser_id' : request.session['authuser']['id']}
    return render(request, 'board/write.html', context)


def delete(request):
    board = Board()
    board.id = request.POST.get('id', request.GET.get('id'))
    instance = Board.objects.filter(id=board.id).get()
    instance.delete()

    return HttpResponseRedirect('/board')