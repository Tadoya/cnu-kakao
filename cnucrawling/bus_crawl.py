import requests
from bs4 import BeautifulSoup

# def get_bus_info(call):
#     str = ''
#     crawl_json = crawl()
#
#     print('called by', call)
#     for key in crawl_json:
#         str += key+'\n\t'+crawl_json[key]+'\n\n'
#
#     print(str)
#     return str

def crawl():
    try:
        req = requests.get('http://plus.cnu.ac.kr/html/kr/sub05/sub05_050403.html')
    except:
        return 'error'

    html = req.content.decode('utf-8', 'replace').encode('euc-kr', 'replace')
    soup = BeautifulSoup(html, 'lxml')

    my_titles = soup.find_all('ul', class_='h8_ul')

    data=[]

    i = 0
    for title in my_titles:
        data.append(title.text)
        print(i, title.text)
        i+=1


    print(4,data[4].split(),'\n')
    print(5,data[5].split(),'\n')
    print(6,data[6].split(),'\n')
    print(7,data[7].split(),'\n')


##너무 비효율
#     return make_bus_json(name, data)
#
#
# #크롤링한 도서관좌석정보를 Josn화
# def make_bus_json(name, data):
#     bus_info = {}
#     for i in range(1, 12):
#         library_info[make_library_json_key(data, i)] = data[i].split()[5] + '/' + data[i].split()[4] + '(' + data[i].split()[6] + ') ' + data[i].split()[7]
#
#     library_info['전자정보실'] =  data[13].split()[2] + '/' + data[13].split()[1] + '(' + data[13].split()[3] + ') ' + data[13].split()[4]
#     return bus_info