"""
The documentation original implementations can be found here:
https://blog.51cto.com/devops2016/2084084
"""

import cv2
img = cv2.imread('background.jpg')
arr=[]
def show_xy(event,x,y,flags,userdata):
    if flags == 1:
        arr.append([x,y])
    # 印出相關參數的數值，userdata 可透過 setMouseCallback 第三個參數垂遞給函式

cv2.imshow('stroke', img)
cv2.setMouseCallback('stroke', show_xy, arr)  # 設定偵測事件的函式與視窗

cv2.waitKey(0)     # 按下任意鍵停止
cv2.destroyAllWindows()
print(arr)