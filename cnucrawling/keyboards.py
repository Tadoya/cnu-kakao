#keyboard

def default_keyboard():
    return {
        'type' : 'buttons',
        'buttons' : ['학식', '도서관', '버스노선']
    }

def bus_keyboard():
    return {
        'type' : 'buttons',
        'buttons' : ['A노선(경상)', 'B노선(사회)', 'C노선(유성)', 'D노선(야간)', '보운(편도)', '보운(운행)']
    }

def nonbutton_keyboard():
    return {
        'type' : 'text',
    }