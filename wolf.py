import cv2

picture=cv2.imread("wolf.jpg" , 0 )


h ,w =picture.shape

for i in range(h):

    for j in range(w):

        if picture[i][j] < 100 :

            picture[i][j] = 0


cv2.imwrite("wolf1.jpg", picture)
 
cv2.waitKey()

