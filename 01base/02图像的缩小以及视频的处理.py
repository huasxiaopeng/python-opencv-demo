import cv2 as cv
img=cv.imread("../Resources/Photos/cat_large.jpg")
# cv.imshow("cat",img)
# 调整函数
def rescalframe(frame,scale=0.74):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

# 调整图片的大小
resized_img=rescalframe(img)
cv.imshow("resize_cat",resized_img)


capture=cv.VideoCapture("../Resources/Videos/dog.mp4")
while True:
    isTrue,frame=capture.read()
    frame_resized=rescalframe(frame,0.2)
    # cv.imshow("video",frame)
    cv.imshow("revideo",frame_resized)

    if cv.waitKey(20)&0xFF==ord('d'):
       break

capture.release()
cv.destroyAllWindows()