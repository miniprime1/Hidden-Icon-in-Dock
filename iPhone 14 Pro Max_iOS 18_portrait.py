import cv2

img = cv2.imread("input.jpeg", cv2.IMREAD_COLOR)

icon1 = img[2499:2690, 105:296]
icon2 = img[2499:2690, 401:592]
icon3 = img[2499:2690, 697:888]
icon4 = img[2499:2690, 993:1184]

cv2.imwrite("icon1.png", icon1)
cv2.imwrite("icon2.png", icon2)
cv2.imwrite("icon3.png", icon3)
cv2.imwrite("icon4.png", icon4)
