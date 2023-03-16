import cv2

cascade = cv2.CascadeClassifier('C:/Users/koheidoi/AppData/Local/Programs/Python/Python38/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
mask = 'youkai_backbeard.png'
mask_img = cv2.imread(mask)
mask_img = cv2.resize(mask_img, None, fx = 0.2, fy = 0.2)
height, width = mask_img.shape[:2]

cap = cv2.VideoCapture(0)

print('face ready...🍹')

if cap.isOpened():
    print("camera ok 👍")
else:
    print("no")

while(cap.isOpened()):
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    lists = cascade.detectMultiScale(gray, minSize=(5, 5))
    for(x,y,w,h) in lists:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), thickness=2)
        y=(y+h)//2
        x=(x+w)//2
        frame[y:height+y, x:width+x] = mask_img
    cv2.imshow('camera', cv2.flip(frame, 1))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
