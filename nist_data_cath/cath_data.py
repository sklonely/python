
import struct
from bitarray import bitarray
from decimal import *


def getBin(x): return x > 0 and str(bin(x))[2:] or "-" + str(bin(x))[3:]


# 超變數
bytesNum = 5  # 取第幾個
Max_cath_bit = 10000000  # 收集資料量
getcontext().prec = 32  # 小數點後幾位
# 混沌系統變數宣告
x1 = 0.4
x2 = -0.2
x3 = 0.2
x1n = 0
x2n = 0
x3n = 0


def floatToBinary64(value):
    val = struct.unpack('Q', struct.pack('d', value))[0]
    val = getBin(val)
    if value >= 0:
        val = "0"+val
    return val


def binaryToFloat(value):
    hx = hex(int(value, 2))
    return struct.unpack("d", struct.pack("q", int(hx, 16)))[0]


# floats are represented by IEEE 754 floating-point format which are
# 64 bits long (not 32 bits)
# 渾沌亂數生成
count = 1
U_count = 1
file_bitarray = bitarray()
while(Max_cath_bit >= count):

    if U_count == 1000000:
        print(x2, U_count)

    x1n = 0.9853*x1+0.0149*x2
    x2n = 0.0208*x1+0.9994*x2-0.001*x1*x3
    x3n = 0.9973*x3+0.001*x1*x2
    x1 = x1n
    x2 = x2n
    x3 = x3n
    #
    binstr = floatToBinary64(x2)
    hexs = hex(int(binstr, 2))[2:]

    # 寫入文件
    for i in range(8):
        # print(binstr[i+(bytesNum-1)*8],end="")
        if binstr[i+(bytesNum-1)*8] == '1':
            file_bitarray.append(True)
        else:
            file_bitarray.append(False)
        count += 1
    U_count += 1


with open('data.bin', 'ab') as f:
    file_bitarray.tofile(f)
with open('data.txt', 'a+') as f:
    f.write(str(file_bitarray)[10:-2])
print("bits 總長度", len(file_bitarray))
# print(str(file_bitarray)[10:-2])
# print(binstr.from_bytes())
# for i in range(64):
#     print(binstr[i],end='')
# for i in range(len(hexs)):
#     print(hexs[i],end="")
#     if i %2:
#         print()

# print(hexs)
# for i in range(len(binstr)):
#     if i %8 == 0 and i != 0:
#         print(" ",end="")
#     if i == 16:
#         print("s",end="")
#     print(binstr[i],end="")
# print()
