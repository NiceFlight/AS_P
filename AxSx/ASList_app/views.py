from django.shortcuts import render
from regex import P
from SiAs_app.models import SinicaArchaeologySites
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def ASList(request):

    AllAs = SinicaArchaeologySites.objects.using("default").all().order_by("code")

    paginator = Paginator(AllAs, 20)
    # print(dir(paginator))

    page_number = request.GET.get("page")

    try:
        # 獲取該頁的 Page 物件
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        # 如果頁碼不是整數，則顯示第一頁
        page_obj = paginator.page(1)
    except EmptyPage:
        # 如果頁碼超出範圍 (e.g., 第 999 頁)，則顯示最後一頁
        page_obj = paginator.page(paginator.num_pages)

    # for post in page_obj:
    #     print(dir(post))

    context = {"name": "Si List", "page_obj": page_obj}

    return render(request=request, template_name="aslist.html", context=context)
