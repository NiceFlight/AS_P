from django.http import HttpResponse
from django.shortcuts import render
from .models import TempSites


# def adddata(request):
#     context = {
#         "name": "Add New Data"
#     }
#     return render(request, 'adddata.html', context=context)


def adddata(request):
    if request.method == "POST":
        try:
            cname = request.POST.get("cname")
            ctype = request.POST.get("ctype")
            description = request.POST.get("des")
            year = request.POST.get("year")
            latitude = request.POST.get("lat")
            longitude = request.POST.get("lng")
            note = request.POST.get("note")
            county = request.POST.get("selectedCity")
            # print(county)
            town = request.POST.get("selectedTown").split("(")[0]
            towncode = request.POST.get("selectedTown").split("(")[1][0:3]
            print(cname, ctype, description, year, latitude, longitude, note, county, town, towncode)
            dataSave = TempSites(
                name=cname,
                type=ctype,
                description=description,
                year=year,
                latitude=latitude,
                longitude=longitude,
                note=note,
                county=county,
                town=town,
                towncode=towncode,
            )
            dataSave.save(using="fourth")
            context = {"message": "資料新增成功"}
            return render(request, "adddata.html", context=context)
        except Exception as e:
            context = {"message": f"資料新增失敗，{e}"}
            return render(request, "adddata.html", context=context)
    else:
        return render(request, "adddata.html")
