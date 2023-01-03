import cv2 as cv

# Build classifier

clf = cv.CascadeClassifier(r'haarcascade_frontalface_default.xml')
camera = cv.VideoCapture(0)  # Laptop camera

while True:
    _, frame = camera.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = clf.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(50, 50),
        flags=cv.CASCADE_SCALE_IMAGE
    )
    for (x, y, width, height) in faces:
        cv.rectangle(frame, (x, y), (x + width, y + height), (255, 255, 0), 2)
    cv.imshow("Faces", frame)
    if cv.waitKey(1) == ord('q'):
        break

camera.release()
cv.destroyAllWindows()
