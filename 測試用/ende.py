def encrypt(key, s):
    """
    type:
    name type
    ---------------
    key  Number
    bs   Str
    --------------
    """
    b = bytearray(str(s).encode("utf8"))
    n = len(b)  # 求出 b 的字节数
    c = bytearray(n)
    j = 0
    key = int(key)
    for i in range(0, n):
        if (b[i] & 128) == 0:
            print("英數 ", b[i], (b[i] + key) % 127)
            c[i] = (b[i] + key) % 127
        elif (b[i] & 240) == 224:
            print("中標頭 ", b[i], end="")
            if b[i] + (key % 16) >= 240:
                c[i] = b[i] + (key % 16) - 240 + 225
                print("", c[i])
            else:
                c[i] = b[i] + (key % 16)
                print("", c[i])
        elif (b[i] & 192) == 128:
            print("跟隨 ", b[i], end="")
            if b[i] + (key % 64) >= 192:
                c[i] = b[i] + (key % 64) - 192 + 128
                print("", c[i])
            else:
                c[i] = b[i] + (key % 64)
                print("", c[i])
    return c


def decode(key, bs):
    """
    type:
    name type
    ---------------
    key  Number
    bs   Str
    --------------
    """
    b = bytearray(bs)
    n = len(b)  # 求出 b 的字节数
    c = bytearray(n)
    j = 0
    key = int(key)
    for i in range(0, n):
        if (b[i] & 128) == 0:
            print("英數 ", b[i])
            c[i] = (b[i] - key) % 127
        elif (b[i] & 240) == 224:
            print("中標頭 ", b[i], end="")
            if b[i] - (key % 16) <= 224:
                print("", b[i] - (key % 16) + 240 - 225)
                c[i] = b[i] - (key % 16) + 240 - 225
            else:
                c[i] = b[i] - (key % 16)
                print("", c[i])
        elif (b[i] & 192) == 128:
            print("跟隨 ", b[i], end="")
            if b[i] - (key % 64) <= 128:
                c[i] = b[i] - (key % 64) + 192 - 128
                print("", c[i])
            else:
                c[i] = b[i] - (key % 64)
                print("", c[i])

    return str(c, encoding='utf-8', errors="ignore")


if __name__ == "__main__":
    # eval()
    ss = "123"
    key = 5
    s = encrypt(key, ss)
    # print("加密前:", ss)
    # print()
    tt = str(s)
    # print(tt[10:-1])
    # print(eval(tt))
    print("加密後:", s)
    de = decode(key, s)
    print(de)