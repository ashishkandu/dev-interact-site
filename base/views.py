from django.shortcuts import render
# from django.http import HttpResponse


rooms = [
    {'id': 1, 'name': 'Lets learn Django'},
    {'id': 2, 'name': 'Design Class'},
    {'id': 3, 'name': 'Frontenders !'},

]


def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == pk:
            room = i
            break
    context = {'room': room}
    return render(request, 'base/room.html', context)
