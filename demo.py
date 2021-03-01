import cv2


image = cv2.imread("image.jpg")
while True:
    cv2.imshow("demo", image)
    cv2.waitKey(1)
