from Crypto.Cipher import AES
import hashlib
from PIL import Image
import numpy as np


class AEScharp():

    def __init__(self):
        self._IV = 16 * '\x00'
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

    # 將圖片轉成　整數陣列　回傳
    def picture_to_RGB(self, im):
        array = np.array(im)
        return array

    # 加密 CBC
    def encrypt_CBC_speed(self, data, key, _IV=16 * b'\x00'):
        # 處理密鑰
        key = str(key)
        key = hashlib.sha256(key.encode('utf-8')).digest()
        aes = AES.new(self.pad_key(key), AES.MODE_CBC, _IV)
        # 處理資料
        data = data.encode(encoding="utf-8")
        data = self.pad(data)
        # 加密資料
        return aes.encrypt(data)

    # 解密 CBC
    def decrypt_CBC_speed(self, data, key, _IV=16 * b'\x00'):
        # 處理密鑰
        key = str(key)  # 避免近來數值太奇怪 轉成str
        key = hashlib.sha256(key.encode('utf-8')).digest()  # 將key做utf-8解碼成bytes放入hash
        aes = AES.new(self.pad_key(key), AES.MODE_CBC, _IV)  # 建置AES加密核心 使用key當AESkey 模式CBC _IV
        # 解密資料
        data = str(aes.decrypt(data), encoding='utf-8', errors="ignore")
        # 將資料轉回utf8
        return data

    # 加密 ECB
    def encrypt_ECB(self, data, key):
        # 處理密鑰
        key = str(key)  # 避免近來數值太奇怪 轉成str
        key = hashlib.sha256(key.encode('utf-8')).digest()  # 將key做utf-8解碼成bytes放入hash
        aes = AES.new(self.pad_key(key), AES.MODE_ECB)  # 建置AES加密核心 使用key當AESkey 模式ECB
        # 處理資料 將key做utf-8解碼成bytes補足16bits
        data = data.encode(encoding="utf-8")
        data = self.pad(data)
        # 加密資料
        return aes.encrypt(data)

    # 解密 ECB
    def decrypt_ECB(self, data, key):
        # 處理密鑰
        key = str(key)  # 避免近來數值太奇怪 轉成str
        key = hashlib.sha256(key.encode('utf-8')).digest()  # 將key做utf-8解碼成bytes放入hash
        aes = AES.new(self.pad_key(key), AES.MODE_ECB)  # 建置AES加密核心 使用key當AESkey 模式ECB
        # 解密資料 將data先解密玩 再用utf-8顯示
        data = str(aes.decrypt(data), encoding='utf-8', errors="ignore")
        # 將資料轉回utf8
        return data

    # 加密 ECB bytes
    def encrypt_ECB_by(self, data, key):
        # 處理密鑰
        key = str(key)  # 避免近來數值太奇怪 轉成str
        key = hashlib.sha256(key.encode('utf-8')).digest()  # 將key做utf-8解碼成bytes放入hash
        aes = AES.new(self.pad_key(key), AES.MODE_ECB)  # 建置AES加密核心 使用key當AESkey 模式ECB
        # 處理資料 將key做utf-8解碼成bytes補足16bits
        # data = data.encode(encoding="utf-8")
        # data = self.pad(data)
        # 加密資料
        return aes.encrypt(data)

    # 解密 ECB bytes
    def decrypt_ECB_by(self, data, key):
        # 處理密鑰
        key = str(key)  # 避免近來數值太奇怪 轉成str
        key = hashlib.sha256(key.encode('utf-8')).digest()  # 將key做utf-8解碼成bytes放入hash
        aes = AES.new(self.pad_key(key), AES.MODE_ECB)  # 建置AES加密核心 使用key當AESkey 模式ECB
        # 解密資料 將data先解密玩 再用utf-8顯示
        data = aes.decrypt(data)
        # 將資料轉回utf8
        return data
