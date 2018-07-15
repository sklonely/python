import requests

r = requests.post('http://127.0.0.1:5000/AES_encrypt', data={'data': '123'})
print(r.text)