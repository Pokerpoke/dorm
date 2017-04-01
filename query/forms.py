"""
Forms that get data from database
"""
from django import forms


class DevRoomForm(forms.Form):
    """
    Forms of dev---roomname query
    """
    dev = forms.CharField(label='设备ID', max_length=10)
