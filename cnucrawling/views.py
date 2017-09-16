import json, datetime, time
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import keyboards
from . import library_crawl, bus_info, meal_crawl

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
            'message' :{
                'text' : library_crawl.get_library_info(),
            },
            'keyboard' : keyboards.default_keyboard()
        })

################ 학식

    elif content_msg == "학식":
        return JsonResponse({
            'message' :{
                'text' : '메뉴를 확인할 식당을 선택하세요.'
            },
            'keyboard' : keyboards.meal_keyboard()
        })
    elif content_msg == "취업지원회관" or content_msg == "3후생관" \
        or content_msg == "상록회관" or content_msg == "생활과학회관":
        return JsonResponse({
            'message' :{
                'text' : meal_crawl.get_meal_info(content_msg)
            },
            'keyboard' : keyboards.default_keyboard()
        })
    elif content_msg == "1후생관(링크)":
        return JsonResponse({
            'message' : {
                'text' : '링크를 누르면 메뉴화면이 나타납니다.'
            },
            'message_button':{
                'label' : '자세히보기',
                'url' : 'http://cnuis.cnu.ac.kr/jsp/etc/foodcourt1005.jpg'
            },
            'keyboard' : keyboards.default_keyboard()
        })

############### 버스


    elif content_msg == "버스노선":
        return JsonResponse({
            'message' :{
                'text' : '노선을 선택하세요.'
            },
            'keyboard' : keyboards.bus_keyboard()
        })
    elif content_msg =="A노선(경상)":
        return JsonResponse({
            'message' :{
                'text' : bus_info.get('A')
            },
            'keyboard' : keyboards.default_keyboard()
        })
    elif content_msg =="B노선(사회)":
        return JsonResponse({
            'message' :{
                'text' : bus_info.get('B')
            },
            'keyboard' : keyboards.default_keyboard()
        })
    elif content_msg =="C노선(유성)":
        return JsonResponse({
            'message' :{
                'text' : bus_info.get('C')
            },
            'keyboard' : keyboards.default_keyboard()
        })
    elif content_msg =="D노선(야간)":
        return JsonResponse({
            'message' :{
                'text' : bus_info.get('D')
            },
            'keyboard' : keyboards.default_keyboard()
        })
    elif content_msg =="보운(편도)":
        return JsonResponse({
            'message' :{
                'text' : bus_info.get('E')
            },
            'keyboard' : keyboards.default_keyboard()
        })
    elif content_msg =="보운(운행)":
        return JsonResponse({
            'message' :{
                'text' : bus_info.get('F')
            },
            'keyboard' : keyboards.default_keyboard()
        })
    else:
        return JsonResponse({
            'message' :{
                'text' : 'error'
            },
            'keyboard' : keyboards.default_keyboard()
        })