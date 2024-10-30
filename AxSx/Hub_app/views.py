from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import pymysql
import pymysql.cursors
from Hub_app.models import AirportsData
import json
from decimal import Decimal


def hubmap(request):

    #  查詢出 hub 
    hubs = AirportsData.objects.using('second').filter(hub=1).values('name', 'country', 'city', 'lat', 'lng')
    # print(type(hubs))
    hubs_list = []
    for hub in hubs:
        hubs_list.append({
            'name': hub['name'], 
            'country': hub['country'], 
            'lat': float(hub['lat']) if hub['lat'] is not None else None, 
            'lng': float(hub['lng']) if hub['lng'] is not None else None, 
            'city': hub['city'], 
        })
    hubs_json = json.dumps(hubs_list)

    # 查詢出 base
    base = AirportsData.objects.using('second').filter(base=1)
    base_list=[]
    for b in base:
        base_list.append({
        'name': b.name, 
        'lat': float(b.lat) if b.lat is not None else None, 
        'lng': float(b.lng) if b.lng is not None else None, 
        'country': b.country, 
        'city': b.city, 
        })
    base_json = json.dumps(base_list)
    context = {
        'hubs_json': hubs_json, 
        'base_json': base_json, 
    }
    # print(type(context))
    return render(request, 'hubmap.html', context=context)
