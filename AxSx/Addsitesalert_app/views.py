from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import addsitesalertForm

def addsitesalert(request):
    if request.method == 'POST':
        form = addsitesalertForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '資料新增成功')
        else:
            messages.error(request, '資料新增失敗')
        return redirect('addsitesalert')
    else:
        form = addsitesalertForm()
        context = {
            'form': form, 
            'name': 'Add Sites Alert'
        }
    return render(request, 'addsitesalert.html', context)
