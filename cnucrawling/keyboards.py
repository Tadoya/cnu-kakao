#keyboard

def default_keyboard():
    return {
        'type' : 'buttons',
        'buttons' : ['오늘의학식', '열람실현황', '오늘의날씨','학교버스노선']
    }

def bus_keyboard():
    return {
        'type' : 'buttons',
        'buttons' : ['A노선(경상)', 'B노선(사회)', 'C노선(유성)', 'D노선(야간)', '보운(편도)', '보운(운행)']
    }

def meal_keyboard():
    return {
        'type' : 'buttons',
        'buttons' : ['취업지원회관', '3후생관', '상록회관', '생활과학대학', '1후생관(링크)']
    }

def nonbutton_keyboard():
    return {
        'type' : 'text',
    }