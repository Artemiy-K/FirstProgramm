from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
hol_sl = {"01012022":["Нью ер"], "02012022":["Всемирный день интроверта"],"09022022":["День рождения стриптиза"],
          "18022022":["День батарейки"],"18062022":["Всемирный день хот дога", "это про тебя"], "07102022": ["Всемирный день яйца"],
          "18122022":["Всемирный день рождения легендарного Коршак Артёма Дмитровича 2006 года рождения в городе Рубежное и ставший сеньеором в германии более потробно о его биографии вы можете найти тут"]}
def index(request):
    now = datetime.datetime.now()
    day = str(now.day)
    if len(day) != 2:
        day = '0' + day
    month = str(now.month)
    if len(month) == 1:
        month = "0" + month
    year = str(now.year)
    date = day + month + year

    if date in hol_sl:
        s = hol_sl[date]
    else:
        s = "Бухич отменяется... Праздника не будет:("
    return HttpResponse(s)
