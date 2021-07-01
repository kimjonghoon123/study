
import json


# with open(r'C:\Users\kjh19\OneDrive\바탕 화면\cmder\study', 'youtu2') as f:
#     json_data = json.load(f)
#
#     print(json.dumps(json_data))

json_data = open(r'C:\Users\kjh19\OneDrive\바탕 화면\cmder\study\youtu2.json', encoding='UTF8').read()
print(json_data)
for i in range(1000):
    print(json_data[i])
