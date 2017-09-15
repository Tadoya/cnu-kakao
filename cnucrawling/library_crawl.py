import requests
from bs4 import BeautifulSoup

def get_library_info():
    str = ''
    crawl_json = crawl()
    for key in crawl_json:
        str += key+':'+crawl_json[key]+'\n'
    return str

def crawl():
    try:
        req = requests.get('http://clicker.cnu.ac.kr/Clicker/k/')
    except:
        return 'error'

    html = req.text
    soup = BeautifulSoup(html, 'lxml')

    my_titles =soup.select('tr')
    # print('mytitle', my_titles)
    data=[]

    i=0
    for title in my_titles:
        data.append(title.text)
        # print(i, title.text)
        i+=1
    # j=0
    # for num in data[13].split():
    #     print(j, num)
    #     j+=1

    # print(data[1].split()[0][0:1])
    # if name == "도서관":
    return make_library_json(data)



def make_library_json(data):
    library_info = {}
    for i in range(1, 12):
        library_info[make_library_json_key(data, i)] = data[i].split()[5] + '/' + data[i].split()[4] + '(' + data[i].split()[6] + ') ' + data[i].split()[7]

    library_info['전자정보실'] =  data[13].split()[2] + '/' + data[13].split()[1] + '(' + data[13].split()[3] + ') ' + data[13].split()[4]
    return library_info

def make_library_json_key(data, i):
    if len(data[i].split()[3])==1:
        return data[i].split()[0][0:1]+'-'+data[i].split()[2][0:1]+data[i].split()[3]
    else:
        return data[i].split()[0][0:1] + '-' + data[i].split()[2][0:1] +' '+data[i].split()[3]