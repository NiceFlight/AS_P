from django.shortcuts import render, redirect
from .forms import addsitesForm


def addsites(request):
    if request.method == "POST":
        form = addsitesForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "sitesadded.html", {"name": "資料新增成功"})
    else:
        form = addsitesForm()
        context = {"form": form, "name": "Add New Site"}
    return render(request, "addsites.html", context=context)


# def sitesadded(request):
#     if request.method == 'POST':
#         form = addsitesForm(request.POST)
#         if form.is_valid():
#             form.save()
#     return render(request, 'sitesadded.html', {'name': '資料新增成功'})
