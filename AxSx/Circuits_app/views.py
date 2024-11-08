import json
from django.http import JsonResponse
from django.shortcuts import render

def circuits_json(request):
    with open('static/js/f1-circuits.geojson', 'r', encoding='utf-8') as file:
        data = json.load(file)
    # print(data)
    return JsonResponse(data=data)


def circuits(request):
    context = {
        'name': 'Circuits Map', 
    }
    return render(request, 'circuits.html', context)
