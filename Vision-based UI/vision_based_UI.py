import cv2 as cv

backSub = cv.createBackgroundSubtractorMOG2()

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

count = 0
picture = ['cat', 'dog', 'IU', 'Wen-Hung-Liao']
def reshape(img):
    shape = img.shape
    width = 800
    height = int(width * shape[0] / shape[1])
    return cv.resize(img, (width, height))

while True:
    ret, frame = cap.read()
    if frame is None:
        break

    fgmask = backSub.apply(frame)

    #讓鏡頭水平翻轉
    fgmask = cv.flip(fgmask, 1, dst=None)
    frame = cv.flip(frame, 1, dst=None)

    #1th command
    cv.rectangle(frame, (10, 2), (100,50), (220,255,255), -1)
    cv.putText(frame, picture[0], (40, 30), cv.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))
    #2th command
    cv.rectangle(frame, (150, 2), (240,50), (220,255,255), -1)
    cv.putText(frame, picture[1], (177, 30), cv.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))
    #3th command
    cv.rectangle(frame, (290, 2), (380,50), (220,255,255), -1)
    cv.putText(frame, picture[2], (325, 30), cv.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))
    #4th command
    cv.rectangle(frame, (430, 2), (600,50), (220,255,255), -1)
    cv.putText(frame, picture[3], (455, 30), cv.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))

    cv.imshow("Frame", frame)

    count += 1

    #每20偵取樣一次
    if count == 20:
        sum = []
        for i in range(4):
            sum.append(fgmask[2:50, (10 + i*130):(100+ i*130)].sum())
            count = 0
        index = [i for i in range(4) if sum[i] > 5000]
        if len(index) >= 2 or len(index) == 0 or sum[index[0]] < 30000:
            continue
        else:
            getImg = cv.imread('./images/' + picture[index[0]] + '.jpg')
            getImg = reshape(getImg)
            cv.imshow(picture[index[0]], getImg)
            cv.waitKey()
            cv.destroyWindow(picture[index[0]])

        count = 0
        
    #按q退出
    if cv.waitKey(1) == ord('q'):
        break