from django.shortcuts import render
from django.shortcuts import redirect

from query.forms import DevRoomForm

# Create your views here.


def index(request):
    form = DevRoomForm()
    card1 = {'title': '开灯',
             'color': 'blue',
             'content': 'Turn on your light.',
             'action1': {'url': '/queryall/', 'name': '查询'},
             'action2': {'url': '/queryall/', 'name': '查询'}}
    card2 = {'title': '开灯',
             'color': 'green',
             'content': 'Turn on your light.',
             'action1': {'url': '/queryall/', 'name': '查询'},
             'action2': {'url': '/queryall/', 'name': ''}}
    cards = []
    cards.append(card1)
    cards.append(card2)
    return render(request, 'index.html', locals())
