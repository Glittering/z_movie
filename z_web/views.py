from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core.paginator import Paginator
from django.core.serializers import serialize
import json

from z_web.models import * 

# Create your views here.
def movies(request):
    page_id = int(request.GET.get("page", 1))
    mvs = Movie.objects.all()
    
    paginator = Paginator(mvs, 5)
    if page_id <= 0 or page_id > paginator.num_pages:
        return JsonResponse({"status": "page error."}, safe=False)
    page = paginator.page(page_id)
    ser = serialize("json", page)

    return JsonResponse(json.loads(ser), safe=False)
