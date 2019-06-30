
import requests, json

r = requests.get('https://www.douban.com/')
print(r.status_code)

res = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
print(res)