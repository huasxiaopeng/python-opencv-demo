import  cv2 as cv

# 读取图片
# img=cv.imread("../Resources/Photos/cat.jpg")
# # 窗口展示
# cv.imshow("cat",img)
# 读取视频
# 一帧帧的去读取
capture=cv.VideoCapture("../Resources/Videos/dog.mp4")
while True:
    isTrue,frame=capture.read()
    cv.imshow("video",frame)

    if cv.waitKey(20)&0xFF==ord('d'):
       break

capture.release()
cv.destroyAllWindows()


