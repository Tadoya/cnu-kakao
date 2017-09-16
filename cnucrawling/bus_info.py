def get(name):
    if name == 'A노선(경상)':
        return a
    elif name == 'B노선(사회)':
        return b
    elif name == 'C노선(유성)':
        return c
    elif name == 'D노선(야간)':
        return d
    elif name == '보운(편도)':
        return e
    elif name == '보운(운행)':
        return f
    else:
        return 'bus info error'



a = 'A노선(동문주차장)\n' \
    '>운행간격(15분)\n' \
    '\t08:20~11:30,\n' \
    '\t12:45~17:55\n' \
    '>운행노선\n' \
    '①정심화국제문화회관→②경상대학앞→③도서관 앞(농대방향)→④학생생활관3거리→⑤농업생명과학대학 앞→⑥동문주차장→⑦농업생명과학대학 앞→⑧도서관앞(도서관 삼거리 방향)→⑨예술대학앞→⑩음악 2호관앞→⑪공동동물실험센터 입구(회차)→⑫체육관 입구→⑬서문(공동실험실습관앞)→⑭사회과학대학 입구(한누리회관뒤)→⑮산학연교육연구관앞→⑯정심화국제문화회관\n' \
    '\n* 08:20 1회만 월평역에서 출발'

b = 'B노선(동문주차장)\n' \
    '>운행간격(10분)\n' \
    '\t08:30~11:40,\n' \
    '\t12:50~17:55\n' \
    '>운행노선\n' \
    '①정심화국제문화회관→②사회과학대학입구(한누리회관뒤)→③서문(공동실험실습관앞)→④음악2호관앞→⑤공동동물실험센터입구(회차)→⑥체육관입구→⑦예술대학앞→⑧도서관앞(대학본부옆농대방향)→⑨농업생명과학대학 앞→⑩동문주차장→⑪농업생명과학대학앞→⑫학생생활관3거리→⑬도서관앞(도서관삼거리 방향)→⑭공과대학앞→⑮산학연교육연구관앞→⑯정심화국제문화회관\n' \
    '\n* 08:30 1회만 월평역에서 출발'

c = 'C노선(골프학습장 주차장)\n' \
    '>운행간격(60분)\n' \
    '\t08:10~11:50\n' \
    '\t13:10~17:50\n' \
    '>운행노선\n' \
    '①골프연습장주차장(출발)→②도서관앞→③산학연구관→④GS주유소→⑤유성온천역 4번출구 옆 시내버스정류장→⑥유성온천역(7번)→⑦정심화국제문화회관→⑧도서관→⑨골프연습장주차장' \
    '\n* 오전․오후 막차는 각각11:50 및 17:50분으로 조정하여 운행)'

d = 'D노선(정심화국제문화회관)\n' \
    '>운행간격(30분\)\n' \
    '\t상행(19:00~23:00)\n' \
    '\t하행(19:15~23:15)\n' \
    '>상행 노선\n' \
    '①정심화국제문화회관(출발)→②도서관→③학생생활관' \
    '>하행 노선\n' \
    '①학생생활관(출발)→②도서관→③정심화국제문화회관'

e = '보운캠퍼스 노선\n' \
    '>운행시간(08:10)\n' \
    '  한 주에 4회 편도 운행\n' \
    '  (화 1대, 수 1대, 금 2대)\n' \
    '>노선\n' \
    '①대덕캠퍼스 골프연습주차장→②도서관 앞→③보운캠퍼스(문화동)\n'

f = '보운캠퍼스 운행 내역(학교버스)' \
    '>운행시간\n' \
    '\t08:10, 10:00\n' \
    '\t13:00, 16:00\n' \
    '>운행노선\n' \
    '①골프연습장주차장→②영탑지→③산학연교육연구관→④온천역(1번)→⑤롯데백화점(버스정류장)→⑥서대전역(버스정류장)→⑦충남대병원(의대앞버스정류장)→⑧서대전4거리→⑨중도일보(건너편버스정류장)→⑩갈마동4거리→⑪갈마초등학교3거리→⑫누리아파트105동3거리→⑬진달래아파트107동버스정류장→⑭정심화국제문화회관→⑮도서관→⑯골프연습장주차장'