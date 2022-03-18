import math , requests
def grid(v1, v2) : 
    RE = 6371.00877 # 지구 반경(km) 
    GRID = 5.0 # 격자 간격(km) 
    SLAT1 = 30.0 # 투영 위도1(degree) 
    SLAT2 = 60.0 # 투영 위도2(degree) 
    OLON = 126.0 # 기준점 경도(degree) 
    OLAT = 38.0 # 기준점 위도(degree) 
    XO = 43 # 기준점 X좌표(GRID) 
    YO = 136 # 기1준점 Y좌표(GRID) 
    DEGRAD = math.pi / 180.0 
    RADDEG = 180.0 / math.pi 
    re = RE / GRID; slat1 = SLAT1 * DEGRAD 
    slat2 = SLAT2 * DEGRAD 
    olon = OLON * DEGRAD 
    olat = OLAT * DEGRAD 
    sn = math.tan(math.pi * 0.25 + slat2 * 0.5) / math.tan(math.pi * 0.25 + slat1 * 0.5) 
    sn = math.log(math.cos(slat1) / math.cos(slat2)) / math.log(sn) 
    sf = math.tan(math.pi * 0.25 + slat1 * 0.5) 
    sf = math.pow(sf, sn) * math.cos(slat1) / sn 
    ro = math.tan(math.pi * 0.25 + olat * 0.5) 
    ro = re * sf / math.pow(ro, sn); rs = {}; ra = math.tan(math.pi * 0.25 + (v1) * DEGRAD * 0.5) 
    ra = re * sf / math.pow(ra, sn) 
    theta = v2 * DEGRAD - olon 
    if theta > math.pi : 
        theta -= 2.0 * math.pi 
    if theta < -math.pi : 
        theta += 2.0 * math.pi 
    theta *= sn 
    rs['x'] = math.floor(ra * math.sin(theta) + XO + 0.5) 
    rs['y'] = math.floor(ro - ra * math.cos(theta) + YO + 0.5) 
    params ={'serviceKey' : "fnUVOlpl/AI3PI68GPk7oS9fLaNhOlQU/Qyqd4pjvafLwNytU8d1pGzfGOUucVC7puiyArVzz2qS5xJJeNxtpg==",\
     'pageNo' : '1', 'numOfRows' : '1000', 'dataType' : 'JSON', 'base_date' : '20220318', 'base_time' : '1400', 'nx' : str(rs["x"]).split('.')[0], 'ny' : str(rs["y"]).split('.')[0] }
    return params
if __name__ == "__main__" : 
    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'

    response = requests.get(url, grid(35.45868, 129.36669)).json()
    print(response['response']['body']['items']['item'])


