import cv2
print(cv2.data.haarcascades)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
if face_cascade.empty():
    print("Error: Cascade file not loaded")
    exit()
#cap=cv2.VideoCapture(1)
cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)
cv2.namedWindow("Face Detection - Press q to Quit", cv2.WINDOW_NORMAL)
if not cap.isOpened():
    print('Error: Could not open camera.')
    exit()
while True:
    ret,frame=cap.read()
    if not ret:  
        print('Error: Failed to capture image')
        break
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    for (x, y, w, h) in faces:
        cv2.circle(frame,(x,y),(int(3.14(x+w,y+h))),(255,0,255),2)
    cv2.imshow('Face Detection - Press q Quit',frame)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()