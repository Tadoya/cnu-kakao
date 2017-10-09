import requests, datetime
from bs4 import BeautifulSoup

#문자열화
def get():

    nowtime = timeset(datetime.datetime.now().hour)+'시'+str(datetime.datetime.now().minute)+'분'
    info ='열람실 좌석현황\n('+nowtime+')\n\t잔여좌석/전체좌석\n\n'
    crawl_json = crawl()

    for key in crawl_json:
        info += '>'+key+'\n\t'+crawl_json[key]+'\n\n'

    return info

def crawl():
    try:
        req = requests.get('http://clicker.cnu.ac.kr/Clicker/k/')
    except:
        return 'error'

    html = req.text
    soup = BeautifulSoup(html, 'lxml')
    selected_elements =soup.select('div.maincontent table tbody tr')


    data=[]
    td_count=0
    # 태그제거
    for element in selected_elements:
        data.append(element.text)
        # print(td_count, element.text)
        td_count+=1


    return make_library_json(data)


#크롤링한 도서관좌석정보를 Josn화
def make_library_json(data):
    library_info = {}
    for i in range(0, 11):
        library_info[make_library_json_key(data, i)] = data[i].split()[5] + '/' + data[i].split()[4] + '(' + data[i].split()[6] + ') ' + data[i].split()[7]

    library_info['전자정보실'] =  data[11].split()[2] + '/' + data[11].split()[1] + '(' + data[11].split()[3] + ') ' + data[11].split()[4]
    return library_info

#크롤링한 좌석정보를 Json화 할 때 key 값만들기 (ex: 2-1A)
def make_library_json_key(data, i):
    return data[i].split()[0] +' 제 '+ data[i].split()[2] + ' ' + data[i].split()[3]


def timeset(nowhour):
    if (nowhour/12)>1:
        return '오후 '+str(nowhour%12)
    else:
        return '오전 '+str(nowhour)