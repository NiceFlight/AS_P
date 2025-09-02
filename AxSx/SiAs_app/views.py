from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from SiAs_app.models import SinicaArchaeologySites
import json


def sias(request):
    # sias = SinicaArchaeologySites.objects.all()
    # sias_data = []
    # for _as in sias:
    #     sias_data.append(
    #         {
    #             "name": _as.name,
    #             "code": _as.code,
    #             "des": _as.des if _as.des is not None else None,
    #             "culture_type": (
    #                 _as.culture_type if _as.culture_type is not None else None
    #             ),
    #             "era": _as.era if _as.era is not None else None,
    #             "year": _as.year if _as.year is not None else None,
    #             "rating": _as.rating if _as.rating is not None else None,
    #             "lat": float(_as.lat) if _as.lat is not None else None,
    #             "lng": float(_as.lng) if _as.lng is not None else None,
    #         }
    #     )
    # sias_json = json.dumps(sias_data, ensure_ascii=False)
    # print(sias_json)

    return render(request, "sias.html")


def view_sias(request):
    if request.method == "POST":
        data = json.loads(request.body)
        # print(data)
        city = data.get("filterCity")

        siases = SinicaArchaeologySites.objects.using("default").filter(city=city)
        # print(siases)

        sias_data = []
        for _as in siases:
            sias_data.append(
                {
                    "name": _as.name,
                    "code": _as.code,
                    "des": _as.des if _as.des is not None else None,
                    "culture_type": (_as.culture_type if _as.culture_type is not None else None),
                    "era": _as.era if _as.era is not None else None,
                    "year": _as.year if _as.year is not None else None,
                    "rating": _as.rating if _as.rating is not None else None,
                    "lat": float(_as.lat) if _as.lat is not None else None,
                    "lng": float(_as.lng) if _as.lng is not None else None,
                }
            )
        try:
            with open("static/js/city.geojson", "r", encoding="utf-8") as f:
                data = json.load(f)
                if "台" in city:
                    city = city.replace("台", "臺")
                else:
                    city = city
                # print(city)
                selectedCity = {}
                for i in data["features"]:
                    if i["properties"]["COUNTYNAME"] == city:
                        selectedCity = {"type": "FeatureCollection", "features": [i]}

        except Exception as e:
            print(f"failed: {e}")

        sias_json = json.dumps(sias_data, ensure_ascii=False)
        selectedCity_json = json.dumps(selectedCity, ensure_ascii=False)
        # print(type(sias_json))
        # print(type(selectedCity_json))

    return JsonResponse({"status": "success", "sias_json": sias_json, "selectedCity_json": selectedCity})
