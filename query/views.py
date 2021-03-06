# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from dormdb.models import Dorm

# Create your views here.


@login_required(login_url='/login/')
def queryall(request):
    """
    Query all data from dormdb_dorm database
    """
    dorm = Dorm.objects.order_by('-time')[:10]
    return render(request, 'queryall.html', {'dorm': dorm})


def get_dev(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DevRoomForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return redirect('/queryall/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DevRoomForm()
        return render(request, 'index.html', {'form': form})


def deletedata(request):
    Dorm.objects.all().delete()
    return redirect('/queryall')
