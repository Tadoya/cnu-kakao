from . import meal_crawl

###### form

def get_form(place, data):
    a = '취업지원회관\n' \
        '>학생식단(백반) ' + data[13].split()[0] + '원\n' \
        + make_menu(data[12]) + \
        '\n>교직원식당 ' + data[22].split()[0] + '원\n' \
        + make_menu(data[21]) + \
        '\n>학생식당(일품)\n' \
        + make_menu_ilpum(data[30]) + '\n'

    b = '3후생관 \n' \
        '>학생식단(백반)\n' \
        + make_menu(data[14]) + \
        '\n>교직원식당 ' + data[24].split()[0] + '원\n' \
        + make_menu(data[23])

    c = '상회회관\n' \
        '>학생식단(백반) ' + data[17].split()[0] + '원\n' \
        + make_menu(data[16]) + '\n' \
                                '\n>교직원식당 ' + data[26].split()[0] + '원\n' \
        + make_menu(data[25]) + \
        '\n>학생식당(일품)\n' \
        + make_menu_ilpum(data[32])

    d = '생활과학대학\n' \
        '>학생식단(백반) ' + data[19].split()[0] + '원\n' \
        + make_menu(data[18]) + \
        '\n>교직원식당 ' + data[28].split()[0] + '원\n' \
        + make_menu(data[27]) + \
        '\n>학생식당(일품)\n' \
        + make_menu_ilpum(data[33])


    if place == '취업지원회관':
        return a
    elif place == '3후생관':
        return b
    elif place == '상록회관':
        return c
    elif place == '생활과학대학':
        return d
    else:
        return 'meal error'

def make_menu(data):
    str='\t'
    for key in data.split():
        if key =='(pork' or key=='(beef' or key=='null':
            continue
        elif key =='included)':
            continue
        str += key +'\n\t'

    return str

def make_menu_ilpum(data):
    i=0;
    iscontinue=False
    str='\t'
    for key in data.split():
        if key =='(pork' or key=='(beef' or key=='null':
            continue
        elif key == 'included)':
            iscontinue=True
            continue
        elif iscontinue == True:
            iscontinue=False
            continue

        if i%2==1:
            str += key+'원\n\t'
        else :
            str += key+'\t'
        i += 1

    return str