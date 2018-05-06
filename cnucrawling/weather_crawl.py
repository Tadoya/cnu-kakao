import requests as req
from bs4 import BeautifulSoup

class Weather():
    def __init__(self):
        self.texts = []

    def get_weather_data(self):
        '''
        :return: 궁동 날씨검색결과
        '''

        base_url = 'https://search.daum.net'
        searched_url = base_url+'/search?w=tot&q=대전광역시%20유성구%20궁동%20날씨'

        try:
            res = req.get(searched_url)
            soup = BeautifulSoup(res.text, 'lxml')
            cont_today = soup.select('div.cont_today')[0]
            # 13시 현재, 흐리고 비
            txt_weather = cont_today.select('.txt_weather')[0].text.split(',')
            # 15
            txt_temp = cont_today.select('.txt_temp')[0].text
            # 어제보다 8°C 낮아요.  체감온도 15℃
            txt_desc = cont_today.select('.txt_desc')[0].text

            parsed_dl = cont_today.select('.dl_weather')

            # 현재풍속 1.4m/s
            txt_wind = parsed_dl[0].text.strip()
            # 현재습도 95%
            txt_hum = parsed_dl[1].text.strip()
            # 미세먼지 좋음
            txt_dust = parsed_dl[2].text.strip()

            form = '충남대 날씨는 ' + txt_weather[0] + ',\n' \
                    + txt_weather[1].strip() +' '+ txt_temp + ' \n' \
                    + txt_desc + '\n' \
                    + txt_wind + '\n' \
                    + txt_hum + '\n' \
                    + txt_dust + '\n'

            return form
        except Exception as e:
            print('fail', e)
            return 'fail'

# if __name__ == '__main__':
#     w = Weather()
#     print(w.get_weather_data())