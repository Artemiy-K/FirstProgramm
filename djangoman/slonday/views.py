from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def index(request):
    now = datetime.datetime.now()
    """s = ""

    if now.day == 12 and now.month == 8:
        s = "пора кормить слонов!"
    else:
        s = "Слоны сегодня не едят"
    return render(request, "slonday/index.html", {

        "slday": s
    })"""
    if now.day == 12 and now.month == 8:
        f = True
    else:
        f = False
    return render(request, "slonday/index.html", {

        "slday": 12
    })


def weekday(request):
    now = datetime.datetime.today().weekday()+1

    return render(request, "slonday/index2.html", {
        "day": now
    })


