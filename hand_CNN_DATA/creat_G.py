import cv2
import imutils
import math
import numpy as np
import os

# global variables
bg = None


def init_create_folder_database():
    # create the folder and database if not exist
    if not os.path.exists("train"):
        os.mkdir("train")


def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
# 前後景分離用


def get_hand_hist():
    with open("hist", "rb") as f:
        hist = pickle.load(f)
    return hist


def run_avg(image, aWeight):
    global bg
    # 初始化背景
    if bg is None:
        bg = image.copy().astype("float")
        return

    # 更新背景(影像,背景,更新速度)
    cv2.accumulateWeighted(image, bg, aWeight)


# ---------------------------------------------
# 手位置辨識
# ---------------------------------------------


def segment(image, threshold=25):
    global bg
    # 找出背景與主體差
    diff = cv2.absdiff(bg.astype("uint8"), image)

    # 閾值差異圖像，以便我們得到前景
    thresholded = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)[1]

    # 獲得閾值圖像中的輪廓
    (cnts, _) = cv2.findContours(thresholded.copy(),
                                 cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 沒輪廓就表示沒手
    if len(cnts) == 0:
        return
    else:
        # 找出輪廓中最大的，假設為手
        segmented = max(cnts, key=cv2.contourArea)
        return (thresholded, segmented)


def get_defects(cnt, drawing):
    defects = None
    hull = cv2.convexHull(cnt)
    # print(hull[0][0])
    # cv2.drawContours(drawing, [cnt + (right, top)], 0, (0, 255, 0), 0)
    # cv2.drawContours(drawing, [hull + (right, top)], 0, (0, 0, 255), 1)
    hull = cv2.convexHull(cnt, returnPoints=False)       # For finding defects
    if hull.size > 15:
        defects = cv2.convexityDefects(cnt, hull)
    return defects

# Gesture Recognition


def gesture_recognize(cnt, defects, count_defects, crop_res):
    # use angle between start, end, defect to recognize # of finger show up
    angles = []
    count_defects = 0
    gesture = None

    if defects is not None and cv2.contourArea(cnt) >= 2500:
        # print(cv2.contourArea(cnt))
        for i in range(defects.shape[0]):
            s, e, f, d = defects[i, 0]
            start = tuple(cnt[s][0]+(right, top))
            # if i == 0:
            #     cv2.circle(crop_res, start, 5, [255, 255, 0], -1)
            end = tuple(cnt[e][0]+(right, top))
            far = tuple(cnt[f][0]+(right, top))
            a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
            b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
            c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
            angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 180/math.pi
            if start[1] == len(crop_res)-2 and end[1] == len(crop_res)-2:
                # print(start[1], end[1])
                break
            if angle <= 85:
                angles.append(angle)
                count_defects += 1
                cv2.circle(crop_res, start, 5, [255, 255, 0], -1)
                cv2.circle(crop_res, end, 5, [255, 255, 0], -1)
                cv2.circle(crop_res, far, 5, [0, 0, 255], -1)
            cv2.line(crop_res, start, end, [0, 255, 0], 2)

        if count_defects == 1:
            gesture = 'two'
        elif count_defects == 2:
            gesture = 'three'
        elif count_defects == 3:
            gesture = 'four'
        elif count_defects == 4:
            gesture = 'five'
        elif count_defects == 0:
            if cnt[0][0][0] - cnt[15][0][0] > 15:
                gesture = 'gesture'
            else:
                gesture = 'one'
    # return the result of gesture recognition
    return count_defects, gesture


# -----------------
# MAIN FUNCTION
# -----------------
if __name__ == "__main__":
    # 初始化權重
    aWeight = 0.5

    # 初始化攝影機
    camera = cv2.VideoCapture(0)

    # ROI設定
    top, right, bottom, left = 70, 450, 285, 690

    #
    pic_no = 0
    flag_start_capturing = False
    frames = 0
    total_pics = 1200
    # 背景用的初始化
    num_frames = 0
    # 建立目錄
    init_create_folder_database()
    g_id = input("Enter gesture no.: ")
    g_name = input("Enter gesture name/text: ")
    create_folder("train/"+str(g_id))
    DIR = ("train/"+str(g_id))
    org_no = len([name for name in os.listdir(DIR)
                  if os.path.isfile(os.path.join(DIR, name))])
    while(True):
        # 讀影像
        (grabbed, frame) = camera.read()

        # 調整畫面大小
        frame = imutils.resize(frame, width=700)

        # 翻轉影像
        frame = cv2.flip(frame, 1)

        # 複製處理用的影像
        clone = frame.copy()

        # 獲取原影像的型態 (長寬)
        (height, width) = frame.shape[:2]

        # 抓取roi區域
        roi = frame[top:bottom, right:left]

        # 轉換到GRAY下做高斯
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (7, 7), 0)

       # 更新背景
        if num_frames < 30:
            run_avg(gray, aWeight)
            # 初始幀數+1
            num_frames += 1
            num = 0
            cv2.putText(
                clone, "reset bg plase wait...", (0, 30), 0, 1, (0, 0, 255))
        else:
            # 找手
            hand = segment(gray)

            # 檢查手區域是否存在
            if hand is not None:
                # 分割區域
                (thresholded, segmented) = hand

                # 凸點與凹點比較找出手型
                defects = get_defects(segmented, clone)
                a = gesture_recognize(segmented, defects, 0, clone)
                cv2.putText(clone, a[1], (0, 30), 0, 1, (0, 0, 255))

                if flag_start_capturing:
                    pic_no += 1
                    save_img = cv2.resize(thresholded, (128, 128))
                    cv2.imwrite("train/"+str(g_id)+"/" +
                                str(org_no+pic_no)+".jpg", save_img)
                print(org_no+pic_no)
                cv2.imshow("Thesholded", thresholded)

        # 畫辨識區
        cv2.rectangle(clone, (left, top), (right, bottom), (0, 255, 0), 2)

        cv2.imshow("Video Feed", clone)

        keypress = cv2.waitKey(1) & 0xFF

        # if the user pressed "q", then stop looping
        if keypress == ord("q"):
            break
        if keypress == ord('c'):
            if flag_start_capturing == False:
                flag_start_capturing = True
            else:
                flag_start_capturing = False
                frames = 0
        if flag_start_capturing == True:
            frames += 1
        if pic_no == total_pics:
            break
0
# free up memory
camera.release()
cv2.destroyAllWindows()
