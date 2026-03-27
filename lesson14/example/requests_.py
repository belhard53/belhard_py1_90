import requests

url = 'https://ya.ru/'
unp = '590004723'
# url = f'http://www.portal.nalog.gov.by/grp/getData?unp={unp}&charset=UTF-8&type=json'
res = requests.get(url)

print(res.status_code)
print(res.text)
print(res.json())   