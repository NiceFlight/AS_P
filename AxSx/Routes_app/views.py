from django.shortcuts import render, redirect
from django.http import JsonResponse
import pymysql
from Routes_app.models import AirportsData, Routes
import json
from decimal import Decimal
import glob
import hashlib
from django.contrib.gis.geos import GEOSGeometry


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


def queryset(query):
    airportsset = query
    airportssetList = []
    for _ in airportsset:
        airportssetList.append(
            {
                "name": _.name,
                "iatacode": _.iata_code,
                "country": _.country,
                "lat": float(_.lat) if _.lat is not None else None,
                "lng": float(_.lng) if _.lng is not None else None,
                "city": _.city,
            }
        )

    return airportssetList


def routesmap_json(request):
    """read from mysql database"""
    # data = Routes.objects.using("second").filter(route_type="cargo")  # 讀了解不開啦

    cargo_list = []
    dbsetting = {"host": "localhost", "port": 3306, "user": "root", "password": "204821", "database": "airline_manager"}
    conn = pymysql.connect(**dbsetting)
    with conn.cursor() as cursor:
        cursor.execute("select route,route_type, distance,  ST_AsGeoJson(geom) AS geom_text from routes where route_type = 'cargo'")
        data = cursor.fetchall()
        conn.close()

    for _ in data:
        geodata = {
            "type": "FeatureCollection",
            "features": [{"type": "Feature", "geometry": json.loads(_[3]), "properties": {"start": _[0][:3], "end": _[0][-3:], "distance": _[2]}}],
        }
        # print(geodata)
        cargo_list.append(geodata)

    cargo_geojson = cargo_list

    """read json from fiile"""
    commercial_geojson = routesData("geojson/commercial/*.geojson")
    # cargo_geojson = routesData("geojson/cargo/*.geojson")
    # print(cargo_geojson)

    return JsonResponse({"commercial": commercial_geojson, "cargo": cargo_geojson}, safe=False)


def routesmap(request):

    # 查詢出 hub
    hubs_json = json.dumps(queryset(AirportsData.objects.using("second").filter(hub=1)))

    # 查詢出 base
    base_json = json.dumps(queryset(AirportsData.objects.using("second").filter(base=1)))

    # 查詢出 destionation
    destinations_json = json.dumps(queryset(AirportsData.objects.using("second").filter(destination=1)))

    context = {"hubs_json": hubs_json, "base_json": base_json, "destinations_json": destinations_json}

    return render(request, "routesmap.html", context=context)


def updateDestination(request):

    # 查詢出 hub
    hubs_json = json.dumps(queryset(AirportsData.objects.using("second").filter(hub=1)))

    # 查詢出 base
    base_json = json.dumps(queryset(AirportsData.objects.using("second").filter(base=1)))

    if request.method == "POST":

        validData = "0d60dc25c608adc6f988e81abe10780c3534bc7ae2ebe16421095ae8ae19ca9b"

        data = request.POST.get("updateDestination")
        # print(data)
        iataCode = data[:3] if data else "1234"
        codeData = hashlib.sha256((data[3:] if data else "1234").encode()).hexdigest()
        # print(codeData)
        if codeData == validData and len(iataCode) == 3:
            AirportsData.objects.using("second").filter(iata_code=iataCode).update(destination=1)

            # 查詢出 destionation
            destinations_json = json.dumps(queryset(AirportsData.objects.using("second").filter(destination=1)))

            context = {"hubs_json": hubs_json, "base_json": base_json, "destinations_json": destinations_json, "message": "Update successful!"}

            return render(request, "routesmap.html", context=context)
        else:

            # 查詢出 destionation
            destinations_json = json.dumps(queryset(AirportsData.objects.using("second").filter(destination=1)))
            context = {"hubs_json": hubs_json, "base_json": base_json, "destinations_json": destinations_json, "message": "Update failed!"}

            return render(request, "routesmap.html", context=context)

    # 查詢出 destionation
    destinations_json = json.dumps(queryset(AirportsData.objects.using("second").filter(destination=1)))
    context = {"hubs_json": hubs_json, "base_json": base_json, "destinations_json": destinations_json, "message": "try update again!"}

    return render(request, "routesmap.html", context=context)
