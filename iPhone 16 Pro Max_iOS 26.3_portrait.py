import cv2

img = cv2.imread("input.png", cv2.IMREAD_COLOR)

icon1 = img[2539:2743, 125:329]
icon2 = img[2539:2743, 413:617]
icon3 = img[2539:2743, 703:907]
icon4 = img[2539:2743, 991:1195]

cv2.imwrite("icon1.png", icon1)
cv2.imwrite("icon2.png", icon2)
cv2.imwrite("icon3.png", icon3)
cv2.imwrite("icon4.png", icon4)
