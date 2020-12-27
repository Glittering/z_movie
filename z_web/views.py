from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core.paginator import Paginator
from django.core.serializers import serialize
import json

from z_web.models import * 

# Create your views here.
def movies(request):
    """
    视频api
    :param request:  page
    :return: json_list
    """
    page_id = int(request.GET.get("page", 1))
    mvs = Movie.objects.all().order_by("-pk")
    
    paginator = Paginator(mvs, 5)
    if page_id <= 0 or page_id > paginator.num_pages:
        return JsonResponse({"status": "page error."}, safe=False, status=404)
    page = paginator.page(page_id)
    ser = serialize("json", page)

    return HttpResponse(ser, "application/json")


def index(request):
    """
    返回我的get页面
    :param request:
    :return:
    """
    return render(request, "html/get.html")
