from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
hol_sl = {"01012022":["Нью ер"], "02012022":["Всемирный день интроверта"],"09022022":["День рождения стриптиза"],
          "18022022":["День батарейки"],"18062022":["Всемирный день хот дога"], "07102022": ["Всемирный день яйца"],
          "18122022":["Всемирный день рождения легендарного Коршак Артёма Дмитровича 2006 года рождения в городе Рубежное и ставший сеньеором в германии более потробно о его биографии вы можете найти тут"]}
def index(request):
    pass