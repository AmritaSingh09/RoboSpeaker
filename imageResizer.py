import cv2

image = cv2.imread("my_pic.jpeg", cv2.IMREAD_UNCHANGED)
#cv2.imshow("title", image)
#cv2.waitKey(0)


# % by which image is resized
scale_percent = 50

#calculate the 50% of original dimention
new_width = int(image.shape[1] * scale_percent/100)
new_height = int(image.shape[0] * scale_percent / 100)


# resize image
output = cv2.resize(image, (new_width, new_height))
cv2.imwrite("new_image.jpeg", output)
cv2.waitKey(0)