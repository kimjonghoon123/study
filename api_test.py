import requests
import pprint, json
url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
params ={'serviceKey' : "fnUVOlpl/AI3PI68GPk7oS9fLaNhOlQU/Qyqd4pjvafLwNytU8d1pGzfGOUucVC7puiyArVzz2qS5xJJeNxtpg==",\
     'pageNo' : '1', 'numOfRows' : '1000', 'dataType' : 'JSON', 'base_date' : '20220318', 'base_time' : '1400', 'nx' : '129', 'ny' : '35' }

response = requests.get(url, params=params).json()
pprint.pprint(response['response']['body']['items']['item'])
