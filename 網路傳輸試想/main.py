import os

data = "26124"

with open("高應大創新電子初賽文件搞2.pdf", "rb") as f:
    byte = f.read()

    print("\n原檔資訊:")
    print("\t檔案名稱:", f.name)
    print("\t副檔名:", f.name.split(".")[-1])
    print("\t供需", len(byte), "次傳輸")
    print("\t檔案大小:", len(byte)*8, "位元\n")


def getBin(x): return x > 0 and str(bin(x))[2:] or "-" + str(bin(x))[3:]


def strToBin(data):
    res = []
    for i in data:
        x = getBin(int(i))
        for _ in range(4-len(x)):
            x = "0" + x
        res.append(x)
    return res


print(getBin(int(data)))
print(strToBin(data))


def bytes_to_int(bytes):
    result = 0
    count = 0
    for b in bytes:
        result = result * 256 + int(b)
        count += 1
        print(count)
    return result


newByte = byte.hex()
print("\n壓縮後:")
print("\t供需", len(newByte)/8*4, "次傳輸")
print("\t檔案大小:", len(newByte), "位元\n")

data = b'\x20\x10\xf2'
print(len(data)*8)
tabe = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0,
        "8": 0, "9": 0, "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0}
for i in byte.hex():
    tabe[i] += 1

print(tabe)
