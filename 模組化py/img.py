import cv2
import numpy as np
from matplotlib import pyplot
from AESmod import AEScharp
import math
aes = AEScharp()


# 取像素點跟臨近像素值 [(choose=0,水平),(choose=1,垂直),(choose=2,對角)]
def Correlation_of_adjacent_pixels(img, choose, n):
    (w, h, a) = img.shape
    if n > w * h:
        raise BaseException("取樣點數量大於圖片本身數量")
    else:
        hist = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉灰階
        # 取n筆隨機取樣點
        x_coor = list(np.random.randint(low=0, high=w - 1, size=n))
        y_coor = list(np.random.randint(low=0, high=h - 1, size=n))

        img_o = []
        img_n = []

        if choose == 0:  # 水平取樣
            for i in range(n):
                img_o.append(hist[y_coor[i]][x_coor[i]])
                img_n.append(hist[y_coor[i]][x_coor[i] + 1])

            return img_o, img_n

        elif choose == 1:  # 垂直取樣
            for i in range(n):
                img_o.append(hist[y_coor[i]][x_coor[i]])
                img_n.append(hist[y_coor[i] + 1][x_coor[i]])

            return img_o, img_n
        elif choose == 2:  # 對角取樣
            for i in range(n):
                img_o.append(hist[y_coor[i]][x_coor[i]])
                img_n.append(hist[y_coor[i] + 1][x_coor[i] + 1])

            return img_o, img_n
        else:
            raise BaseException("choose need 0~2.")


# 數學公式程式化 公式在上面說明欄
def coefficient_of_association(x, y):
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    n = len(x)
    up = 0
    sum_x = 0
    sum_y = 0
    for i in range(n):
        up += (x[i] - mean_x) * (y[i] - mean_y)
        sum_x += math.pow((x[i] - mean_x), 2)
        sum_y += math.pow((y[i] - mean_y), 2)
    down = math.sqrt(sum_x * sum_y)
    return up / down


if __name__ == "__main__":
    imgobj1 = cv2.imread('im.png')
    stringData = imgobj1.tostring()

    x = Correlation_of_adjacent_pixels(imgobj1, 0, 10000)  #水平取樣
    print(coefficient_of_association(x[0], x[1]))  #分析
    x = Correlation_of_adjacent_pixels(imgobj1, 1, 10000)
    print(coefficient_of_association(x[0], x[1]))
    x = Correlation_of_adjacent_pixels(imgobj1, 2, 100)
    print(coefficient_of_association(x[0], x[1]))

    e_sss = aes.encrypt_ECB_by(stringData, "1")
    e_sss = np.fromstring(e_sss, dtype='uint8').reshape(imgobj1.shape)

    x = Correlation_of_adjacent_pixels(e_sss, 0, 10000)  #水平取樣
    print(coefficient_of_association(x[0], x[1]))  #分析
    x = Correlation_of_adjacent_pixels(e_sss, 1, 10000)
    print(coefficient_of_association(x[0], x[1]))
    x = Correlation_of_adjacent_pixels(e_sss, 2, 10000)
    print(coefficient_of_association(x[0], x[1]))
    pyplot.plot(x[0], x[1], 'r.')
    pyplot.show()