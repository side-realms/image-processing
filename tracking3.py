import cv2

image = 'face.jpg'
img = cv2.imread(image)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cascade = cv2.CascadeClassifier('C:/Users/koheidoi/AppData/Local/Programs/Python/Python38/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

lists = cascade.detectMultiScale(gray, minSize=(5, 5))

print(lists)

if len(lists):
    for(x,y,w,h) in lists:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), thickness=2)
    cv2.imwrite('result.jpg', img)
