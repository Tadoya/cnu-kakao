import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import keyboards

# Create your views here.

def keyboard(request):
    return JsonResponse(keyboards.default_keyboard())

@csrf_exempt
def message(request):
    json_str = (request.body).decode('utf-8')
    received_json_data = json.loads(json_str)
    content_msg = received_json_data['content']
    return JsonResponse({
        'message' :{
            'text' : content_msg
        },
        'keyboard' : keyboards.default_keyboard()
    })