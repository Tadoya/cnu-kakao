#keyboard
from django.http import JsonResponse

def default_keyboard():
    return JsonResponse({
        'type' : 'button',
        'buttons' : ['학식', '도서관', '버스시간표']
    })

def nonbutton_keyboard():
    return JsonResponse({
        'type' : 'text',
    })