import json
from django.http import JsonResponse
from django.shortcuts import render
import pymysql
import pymysql.cursors
from pymysql import cursors
from Axsx_app.models import TaiwanArchaeologySites, VisitedCount

# def CityTown(request):
#     with open("static\\js\\city_town_ID.json", "r", encoding="utf-8") as f:
#         citytown = json.load(f)
#     print(citytown)
#     return JsonResponse(data=citytown)


def map(request):
    # print("Received a request")  # 添加調試訊息
    visitCount = VisitedCount.objects.latest("count")
    visitCount.count += 1
    # print(f"Updated count: {visitCount.count}")
    visitCount.save()  # 儲存更新後的計數
    context = {"name": "AxSx", "visitCount": int(visitCount.count)}
    return render(request, "map.html", context=context)


def view_AxSx(request):
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
        axsx = TaiwanArchaeologySites.objects.filter(town_id=townID)
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


from django.shortcuts import render

# Create your views here.
