import  cv2 as cv
# Read in an image
img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Park', img)


# 转换成灰度
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)


# 模糊图像
# blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
# 增加模糊度
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)
#图像边缘轮廓
canny=cv.Canny(blur,125,175)
# canny=cv.Canny(img,125,175)
cv.imshow('canny ed',canny)

#放大  轮廓放大
dilated=cv.dilate(canny,(7,7),iterations=3)
cv.imshow("Dilated",dilated)


#图像侵蚀
eroded=cv.erode(dilated,(7,7),iterations=3)
cv.imshow('Eroded', eroded)

# 调整图片
resized=cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)
# 裁减
cropped=img[50:200,200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)