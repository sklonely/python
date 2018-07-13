from Crypto.Cipher import AES
import hashlib


class AEScharp():

    def __init__(self):
        pass

    # 將資料補足16 bit
    def pad(self, text):
        while len(text) % 16 != 0:
            text += b' '
        return text

    # 將key補足32 bit
    def pad_key(self, key):
        while len(key) % 32 != 0:
            key += b' '
        return key

    # 加密
    def encrypt(self, data, key):
        # 處理密鑰
        key = str(key)
        key = hashlib.sha256(key.encode('utf-8')).digest()
        aes = AES.new(self.pad_key(key), AES.MODE_ECB)
        # 處理資料
        data = data.encode(encoding="utf-8")
        data = self.pad(data)
        # 加密資料
        return aes.encrypt(data)

    # 解密
    def decrypt(self, data, key):
        # 處理密鑰
        key = str(key)
        key = hashlib.sha256(key.encode('utf-8')).digest()
        aes = AES.new(self.pad_key(key), AES.MODE_ECB)
        # 解密資料
        data = str(aes.decrypt(data), encoding='utf-8', errors="ignore")
        # 將資料轉回utf8
        return data
