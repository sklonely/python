import requests

r = requests.post('http://127.0.0.1:5000/AES_encrypt', data={'data': '我愛python'})
r = r.json()
print(r["encrypt_text"])
print(r["Um"][0])

data = (("data", r["encrypt_text"]), ("Um", r["Um"]))
r = requests.post('http://127.0.0.1:5000/AES_decrypt', data=data)
print(r.json())