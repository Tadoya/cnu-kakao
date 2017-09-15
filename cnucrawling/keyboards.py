#keyboard

def default_keyboard():
    return {
        'type' : 'buttons',
        'buttons' : ['학식', '도서관', '버스시간표']
    }

def nonbutton_keyboard():
    return {
        'type' : 'text',
    }