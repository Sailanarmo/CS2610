from django.shortcuts import render
from django.http import HttpResponse

import time
import pytz

from datetime import date
from datetime import datetime

# Create your views here.

timeZone = pytz.timezone('US/Mountain')

currDate = date.today()
currTime = datetime.now(timeZone)


def index(request):
    return HttpResponse("Hello World!! "+ "</br>" + "The date is: " + currDate.strftime('%b %d, %Y')
    + ", The time is: " + currTime.strftime('%I:%M %p') + "</br>")
