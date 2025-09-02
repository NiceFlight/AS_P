import json
from django.shortcuts import render
from .models import ShipWreck


def shipwreck(request):
    # 大致找出 24 海浬內的沈船
    shipwrecks1 = (
        ShipWreck.objects.filter(latitude__gte=21.352581438843792)
        .filter(latitude__lte=26.038782669443645)
        .filter(longitude__gte=118.91519559631402)
        .filter(longitude__lte=122.50846912150463)
        .values("shipwreckno", "latitude", "longitude")
    )
    shipwrecks2 = (
        ShipWreck.objects.filter(latitude__gte=20.16257493837388)
        .filter(latitude__lte=21.1888931211711)
        .filter(longitude__gte=116.28420307588877)
        .filter(longitude__lte=117.31550230350388)
        .values("shipwreckno", "latitude", "longitude")
    )
    shipwreck_list1 = []
    shipwreck_list2 = []
    for sw1 in shipwrecks1:
        shipwreck_list1.append(
            {
                "no": sw1["shipwreckno"],
                "lat": float(sw1["latitude"]) if sw1["latitude"] is not None else None,
                "lng": (float(sw1["longitude"]) if sw1["longitude"] is not None else None),
            }
        )
    for sw2 in shipwrecks2:
        shipwreck_list2.append(
            {
                "no": sw2["shipwreckno"],
                "lat": float(sw2["latitude"]) if sw2["latitude"] is not None else None,
                "lng": (float(sw2["longitude"]) if sw2["longitude"] is not None else None),
            }
        )
    shipwreck_list = shipwreck_list1 + shipwreck_list2
    shipwrecks_json = json.dumps(shipwreck_list)
    # print(shipwreck_list2)
    context = {"name": "Ship wreck", "shipwreck_json": shipwrecks_json}
    return render(request, "shipwreck.html", context)
    # return render(request, template_name="shipwreck.html", context=context)
