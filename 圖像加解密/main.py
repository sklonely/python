import cv2
import numpy as np
from matplotlib import pyplot
import math
from AESmod import AEScharp

aes = AEScharp()

if __name__ == "__main__":

    cam = cv2.VideoCapture(0)
    # for i in range(200):
    (ret, img) = cam.read()
    print(img.shape)
    # result, imgencode = cv2.imencode('.png', img)  # 圖片編碼
    # stringData = imgencode.tostring()  # 轉成bytes

    # print("標頭: ", stringData[stringData.find(b'IDATx\x01\xec\xc1'):stringData.find(b'IDATx\x01\xec\xc1') + 20])
    # head = stringData[:stringData.find(b'IDATx\x01\xec\xc1') + 8]

    # print("標尾: ", stringData[stringData.find(b'IEND') - 4:])
    # tail = stringData[stringData.find(b'IEND') - 4:]

    # e_sss = aes.encrypt_ECB_by(stringData[stringData.find(b'IDATx\x01\xec\xc1') + 8:stringData.find(b'IEND') - 4], "1")

    # en_img = head + e_sss + tail

    # d_sss = aes.decrypt_ECB_by(e_sss, '1').rstrip()
    # de_img = head + d_sss + tail
    # # print(stringData == de_img)
    # # en_img = head + e_sss[:len(stringData) - len(en_img)] + tail
    # # print(len(stringData))
    # # sss = aes.encrypt_ECB_by(stringData[stringData.find(b'IDAT') + 4:stringData.find(b'IEND')], "1")

    # # print(sss[-50:sss.find(b'\x00\x00\x00\x00') + 4], sss.find(b'\x00\x00\x00\x00'))
    # # print(stringData[stringData.find(b'IEND') - 50:stringData.find(b'IEND')])

    # # sss = stringData[:stringData.find(b'IDAT') + 4] + sss[:sss.find(b'\x00\x00\x00\x00') + 4] + stringData[stringData.find(b'IEND'):]

    # # # print(stringData[:stringData.find(b'IDAT') + 4], stringData[stringData.find(b'IEND'):])

    # print("IHDR", stringData.find(b'IHDR'), stringData[:stringData.find(b'IHDR') + 4])
    # print("IDAT", stringData.find(b'IDAT'), stringData[stringData.find(b'PLTE'):stringData.find(b'IDAT') + 4])
    # print("IEND", stringData.find(b'IEND'), stringData[stringData.find(b'IEND'):])
    # # # print(stringData[stringData.find(b'IDAT') + 4:stringData.find(b'IEND')])
    # # # print(sss[:50])
    # data = np.fromstring(en_img, dtype='uint8')  # 將接收的資料重組成圖片陣列
    # # x = cv2.imdecode(data, 1)

    # cv2.imshow(u'ORG', data)  # 輸出圖像
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # # 處理PNG AES加密不能顯示問題 卡在  data = np.fromstring(en_img, dtype='uint8')  # 將接收的資料重組成圖片陣列 {libpng error: IDAT: invalid code lengths set}