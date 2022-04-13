# -*- coding: utf-8 -*-
import cv2
import numpy as np

def template_matching_ssd(src, tmp):
    h, w = src.shape
    h2, w2 = tmp.shape

    SSD = np.empty((h - h2, w - w2))
    arr = []

    # 走査
    for dy in range(0, h - h2):
        for dx in range(0, w - w2):
            # 二乗誤差の和を計算
            # 計算方法は調整する必要がある
            diff = (src[dy:dy + h2, dx:dx + w2] - temp)**2
            SSD[dy, dx] = diff.sum()

    print(SSD)

    # 最小ではなく、閾値を定める
    # pt = np.unravel_index(score.argmin(), score.shape)
    for ar in range(len(SSD)):
        for el in range(len(SSD[ar])):
            if SSD[ar, el] < 150:
                arr.append([ar, el])
    # print(arr)
    return (arr)

# main
img = cv2.imread("./sample12.png")
temp = cv2.imread("./sample11.png")
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
temp = cv2.cvtColor(temp, cv2.COLOR_RGB2GRAY)
th =170

ret, gray_thresh = cv2.threshold(gray, th, 255, cv2.THRESH_BINARY)
ret, temp_thresh = cv2.threshold(temp, th, 255, cv2.THRESH_BINARY)

#cv2.imshow("gray",gray_thresh)
#cv2.imshow("temp", temp_thresh)
#cv2.waitKey(0)

h, w = temp.shape

arr = template_matching_ssd(gray_thresh, temp_thresh)

for ar in arr:
    cv2.circle(img, (ar[1], ar[0]), 5, (0, 0, 255), thickness=-1)

cv2.imwrite("re2.png", img)
