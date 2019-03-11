# v = b"\x88\x08\xcd\x0b`\xd1\xb7\xc04\xf6\x7f<\t0\x9b\xc3D\xeaW\xbb\x87\xe9\xc2\x03x\x18\xa1'\xb3d\xc6\x83"
# t = b"\x88\x08\xcd\x0b`\xd1\xb7\xc04\xf6\x7f<\t0\x9b\xc3D\xeaW\xbb\x87\xe9\xc2\x03x\x18\xa1'\xb3d\xc6\x83"

# # print(type(v))
# import codecs
# import hashlib
# import numpy as np
# from AESmod import AEScharp
# from Crypto.Cipher import AES

# print(v[0])
# print(type(v))
# print("len", len(v))
# # for i in v:
# #     print(i)
# v = str(v.hex())

# print(v)
# print(type(v))
# # a = hex(int(v, 16))
# a = bytes.fromhex(v)
# print(a)
# print(codecs.encode(a))

# aes = AEScharp()
# key = hashlib.sha256(("test").encode('utf-8')).digest()
# print("加密前金鑰", key.hex())
# print("密文1", aes.en_ECB(str("123"), key))
# print("密文2", aes.encrypt_ECB(str("123"), key).hex())
# x = b'\x00'
# print(x.hex())
# array_alpha = [133, 53, 234, 241]
# hex_string = "".join("%02x" % b for b in array_alpha)
# print(hex_string)
b = (1, 2, 3)
c = [0, b]
print(c[1][1])