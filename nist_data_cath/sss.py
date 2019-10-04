import struct
from bitarray import bitarray
def getBin(x, bins_num):
    bx = x > 0 and str(bin(x))[2:] or "0" + str(bin(x))[3:]
    for _ in range(bins_num-len(bx)):#補0
        bx = '0'+bx
    return bx

def floatToBinary64(value):
    val = struct.unpack('Q', struct.pack('d', value))[0] #將小數解耦合
    val = getBin(val,8) # 轉二進制
    for _ in range(64-len(val)): #補0
        val = '0'+val
    return val

def test_funtion(value):
    print("-------測試函式-------")
    print("專換前:",value)
    print("IEEE754:",floatToBinary64(value))
    print("長度:",len(floatToBinary64(value)))



if __name__ == "__main__":
    # test_funtion(2.222)
    bytesNum = 6
    binstr=floatToBinary64(1.231)
    file_bitarray = bitarray()
    for i in range(8):
        # print(binstr[i+(bytesNum-1)*8],end="")
        if binstr[i+(7-bytesNum)*8]=='1':
            file_bitarray.append(True)
        else:
            file_bitarray.append(False)

    print(binstr)
    print(file_bitarray)
