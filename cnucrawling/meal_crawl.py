import requests
from bs4 import BeautifulSoup

def crawl(cafeteria):
    try:
        req = requests.get('http://cnuis.cnu.ac.kr/jsp/etc/toDayMenu.jsp')
    except:
        return '학교홈페이지 사정으로 학식내용을 불러올 수 없습니다'

    html = req.text
    soup = BeautifulSoup(html, 'lxml')
    my_title = soup.select('tr')
    data=[]
    cafe_mene=[]

    for title in my_title:
        data.append(title.text)

    print("data",data);