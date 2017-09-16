import requests
from bs4 import BeautifulSoup

def get_meal_info(place):
    try:
        req = requests.get('http://cnuis.cnu.ac.kr/jsp/etc/toDayMenu.jsp')
    except:
        return '학교홈페이지 사정으로 학식내용을 불러올 수 없습니다'

    html = req.text
    soup = BeautifulSoup(html, 'lxml')
    my_title = soup.select('table.tab_color tr td')
    data=[]

    #휴일엔 td가 31개 평일엔 43개->월요일에 확인예정
    # td_count=0
    for title in my_title:
        data.append(title.text)
    #     td_count+=1

    # 주말이라서 일단 표에 보이는대로 크롤링
    a = '취업지원회관\n' \
        '>학생식단(백반)\n' \
        + make_menu(data[18])+'\n' \
        '\n>교직원식당\n' \
        + make_menu(data[23])+'\n' \
        '\n>학생식당(일품)\n' \
        + make_menu(data[28])+'\n'

    b = '3후생관\n' \
        '>학생식단(백반)\n' \
        + make_menu(data[19])+'\n' \
        '\n>교직원식당\n' \
        + make_menu(data[24])+'\n' \
        '\n>학생식당(일품)\n' \
        + make_menu(data[29])+'\n'

    c = '상회회관\n' \
        '>학생식단(백반)\n' \
        + make_menu(data[20])+'\n' \
        '\n>교직원식당\n' \
        + make_menu(data[25])+'\n' \
        '\n>학생식당(일품)\n' \
        + make_menu(data[30])+'\n'

    d = '생활과학대학\n' \
        '>학생식단(백반)\n' \
        + make_menu(data[21])+'\n' \
        '\n>교직원식당\n' \
        + make_menu(data[26])+'\n' \
        '\n>학생식당(일품)\n' \
        + make_menu(data[31])+'\n'


    if place=='취업지원회관':
        return a
    elif place=='3후생관':
        return b
    elif place=='상록회관':
        return c
    elif place=='생활과학대학':
        return d
    else: return 'meal error'



def make_menu(data):
    str=''
    if len(data.split())==1:
        return data.split()[0]
    else:
        for i in data:
            str+=data[i]
        return str