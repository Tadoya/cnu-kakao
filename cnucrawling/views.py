import json, datetime, time
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import keyboards
from . import library_crawl

# Create your views here.

def keyboard(request):
    return JsonResponse(keyboards.default_keyboard())

@csrf_exempt
def message(request):
    json_str = (request.body).decode('utf-8')
    received_json_data = json.loads(json_str)
    content_msg = received_json_data['content']

    if content_msg == "도서관":
        return JsonResponse({
            'messgae' :{
             #   'text' : library_crawl.get_library_info('view')
                'text' : '전자정보실 : 60/60(0%) 운영중'
            },
            'keyboard' : keyboards.default_keyboard()
        })
    else:
        return JsonResponse({
            'message' :{
                'text' : content_msg
            },
            'keyboard' : keyboards.default_keyboard()
        })