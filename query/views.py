from django.shortcuts import render

from dormdb.models import Dorm

# Create your views here.


def queryall(request):
    """
    Query all data from dormdb_dorm database
    """
    dorm = Dorm.objects.all().order_by('-time')
    return render(request, 'queryall.html', {'dorm': dorm})
