# Draw a Line on the image

import cv2

image = cv2.imread("Tanjiro&co..jpg")

start_point = (0, 0)
# start coordinate here represents the top left corner of the image

end_point = (250, 250)
# end point represents the bottom right corner of the image

color = (0, 255, 0)
# green color

thickness = 9
# this indicates the thickness of the line

# cv2.line() method helps in creating lines on any particular object

#img = cv2.line(image, start_point, end_point, color, thickness)

cv2.imshow("edited image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()