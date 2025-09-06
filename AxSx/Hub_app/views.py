from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
import pymysql
import pymysql.cursors
from Hub_app.models import AirportsData
import json
from decimal import Decimal
import glob
import hashlib


def routesData(fileDir: str):
    geojsonList = []
    for path in glob.glob(fileDir):
        # print(path)
        try:
            with open(path, "r", encoding="utf-8") as file:
                data = json.load(file)
                geojsonList.append(data)
        except FileNotFoundError:
            print("File not found. Please check the file path.")
    return geojsonList


def hubmap_json(request):
    commercial_geojson = routesData("geojson/commercial/*.geojson")
    cargo_geojson = routesData("geojson/cargo/*.geojson")

    return JsonResponse({"commercial": commercial_geojson, "cargo": cargo_geojson}, safe=False)


def hubmap(request):

    #  查詢出 hub
    hubs = AirportsData.objects.using("second").filter(hub=1).values("name", "country", "city", "lat", "lng", "iata_code")
    # print(type(hubs))
    hubs_list = []
    for hub in hubs:
        hubs_list.append(
            {
                "name": hub["name"],
                "iatacode": hub["iata_code"],
                "country": hub["country"],
                "lat": float(hub["lat"]) if hub["lat"] is not None else None,
                "lng": float(hub["lng"]) if hub["lng"] is not None else None,
                "city": hub["city"],
            }
        )
    hubs_json = json.dumps(hubs_list)

    # 查詢出 base
    base = AirportsData.objects.using("second").filter(base=1)
    base_list = []
    for b in base:
        base_list.append(
            {
                "name": b.name,
                "iatacode": b.iata_code,
                "lat": float(b.lat) if b.lat is not None else None,
                "lng": float(b.lng) if b.lng is not None else None,
                "country": b.country,
                "city": b.city,
            }
        )
    base_json = json.dumps(base_list)

    # 查詢出 destionation
    destinations = AirportsData.objects.using("second").filter(destination=1)
    destination_list = []
    for d in destinations:
        destination_list.append(
            {
                "name": d.name,
                "iatacode": d.iata_code,
                "lat": float(d.lat) if d.lat is not None else None,
                "lng": float(d.lng) if d.lng is not None else None,
                "country": d.country,
                "city": d.city,
            }
        )
    destinations_json = json.dumps(destination_list)

    context = {"hubs_json": hubs_json, "base_json": base_json, "destinations_json": destinations_json}
    # print(type(context))
    return render(request, "hubmap.html", context=context)


def update_hub(request):
    if request.method == "POST":

        validData = "0d60dc25c608adc6f988e81abe10780c3534bc7ae2ebe16421095ae8ae19ca9b"

        data = request.POST.get("updatehub")
        # print(data)
        iataCode = data[:3]
        codeData = hashlib.sha256(data[3:].encode()).hexdigest()
        print(codeData)
        if codeData == validData:
            AirportsData.objects.using("second").filter(iata_code=iataCode).update(destination=1)
            return redirect("hubmap")
        return redirect("hubmap")
    return redirect("hubmap")
