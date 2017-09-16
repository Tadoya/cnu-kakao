import requests
from bs4 import BeautifulSoup

def get_library_info(call):
    str = ''
    crawl_json = crawl()

    print('called by', call)
    for key in crawl_json:
        str += key+' : '+crawl_json[key]+'\n'

    print(str)
    return str

def crawl():
    try:
        req = requests.get('http://clicker.cnu.ac.kr/Clicker/k/')
    except:
        return 'error'

    html = req.text
    soup = BeautifulSoup(html, 'lxml')

    my_titles =soup.select('tr')
    data=[]

    # 테그제거
    for title in my_titles:
        data.append(title.text)

    return make_library_json(data)


#크롤링한 도서관좌석정보를 Josn화
def make_library_json(data):
    library_info = {}
    # for i in range(1, 12):
    #     library_info[make_library_json_key(data, i)] = data[i].split()[5] + '/' + data[i].split()[4] + '(' + data[i].split()[6] + ') ' + data[i].split()[7]

    library_info['전자정보실'] =  data[13].split()[2] + '/' + data[13].split()[1] + '(' + data[13].split()[3] + ') ' + data[13].split()[4]
    return library_info

#크롤링한 좌석정보를 Json화 할 때 key 값만들기 (ex: 2-1A)
def make_library_json_key(data, i):
    if len(data[i].split()[3])==1:
        return data[i].split()[0][0:1]+'-'+data[i].split()[2][0:1]+data[i].split()[3]
    return data[i].split()[0][0:1] + '-' + data[i].split()[2][0:1] +' '+data[i].split()[3]