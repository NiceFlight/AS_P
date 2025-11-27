import json
from django.http import JsonResponse
from django.shortcuts import render
from Axsx_app.models import TaiwanArchaeologySites


# Create your views here.
def maplibre_app(request):

    context = {"name": "maplibre"}
    return render(request, template_name="maplibre.html", context=context)


def view_maplibre(request):
    if request.method == "POST":
        data = json.loads(request.body)
        # print(data)
        townID = data.get("filterTown")
        # print(townID)

        """方法一 - 本機"""
        # try:
        #     connection = pymysql.connect(
        #         host="localhost",
        #         user="root",
        #         password="204821",
        #         database="archaeology",
        #         port=3306,
        #         cursorclass=cursors.DictCursor,
        #     )
        #     with connection.cursor() as cursor:
        #         sql = "SELECT `Name`, `Lat`, `Lng` FROM `taiwan_archaeology_sites` WHERE `Town_ID` = %s"
        #         cursor.execute(sql, townID)
        #         results = cursor.fetchall()
        #         # print(results)
        #     coordinates = [
        #         {"name": row["Name"], "lat": row["Lat"], "lng": row["Lng"]}
        #         for row in results
        #     ]
        #     # print(type(coordinates))
        #     return JsonResponse({"status": "success", "coordinates": coordinates})
        # except pymysql.MySQLError as e:
        #     print(f"Mysql Error: {e}")
        #     return JsonResponse({"status": "error", "error": str(e)}, status=500)
        # except Exception as e:
        #     print(f"錯誤訊息：{e}")
        #     return JsonResponse({"status": "error", "error": str(e)}, status=500)

        """方法一 - Heroku"""
        # try:
        #     connection = pymysql.connect(
        #         host='rtzsaka6vivj2zp1.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
        #         user='s98kcwwgzvam889b',
        #         password='ybf8div1ucg6gerh',
        #         database='j7ztmhqppqqocs7v',
        #         port=3306,
        #         cursorclass=pymysql.cursors.DictCursor
        #     )
        #     with connection.cursor() as cursor:
        #         sql = "SELECT `Name`, `Lat`, `Lng` FROM `taiwan_archaeology_sites` WHERE `Town_ID` = %s"
        #         cursor.execute(sql, townID)
        #         results = cursor.fetchall()
        #         # print(results)
        #     coordinates = [{"name": row['Name'], "lat": row['Lat'], "lng": row['Lng']} for row in results]
        #     # print(type(coordinates))
        #     return JsonResponse({'status': 'success', 'coordinates': coordinates})
        # except pymysql.MySQLError as e:
        #     print(f"Mysql Error: {e}")
        #     return JsonResponse({'status': 'error', 'error': str(e)}, status=500)
        # except Exception as e:
        #     print(f"錯誤訊息：{e}")
        #     return JsonResponse({'status': 'error', 'error': str(e)}, status=500)

        """方法二"""
        axsx = TaiwanArchaeologySites.objects.using("default").filter(town_id=townID)
        coordinates = []
        for asx in axsx:
            coordinates.append({"name": asx.name, "lat": asx.lat, "lng": asx.lng})
        try:
            with open("static/js/town.geojson", "r", encoding="utf-8") as f:
                # print(f"success")
                data = json.load(f)
                filterData = {"type": "FeatureCollection", "features": [f for f in data["features"] if f["properties"]["TOWNID"] == townID]}
                # print(filterData["features"][0]["properties"]["TOWNNAME"])
        except:
            print(f"read failed")
        return JsonResponse(
            {"status": "success", "coordinates": coordinates, "filterData": filterData},
            # json_dumps_params={"ensure_ascii": False},
        )
    else:
        return JsonResponse({"status": "error", "error": "Invalid request method"}, status=400)
