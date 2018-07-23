import requests
import time
times = 0
for i in range(1):
    s = time.time()
    text = "~!@#$%^&*()RRRRRRRRRRRRRRR我不信邪RRRRRRRRRRRRRRR)(*&^%$#@!~"
    r = requests.post('http://127.0.0.1:5000/AES_encrypt', data={'key': "123", 'data': text})
    r = r.json()

    print(r["encrypt_text"])
    print(r["Um"][0])
    data = (("data", r["encrypt_text"]), ("Um", r["Um"]), ("key", "123"))
    r = requests.post('http://127.0.0.1:5000/AES_decrypt', data=data)
    print(r.json()['decrypt_text'])
    e = time.time()
    times += e - s

# print(times / 100)
