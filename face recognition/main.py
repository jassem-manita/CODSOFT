import cv2

harcascade = "model/haarcascade_frontalface_default.xml"
cap = cv2.VideoCapture(0)

cap.set(3, 640)  # Set the width
cap.set(4, 480)  # Set the height

# Load the cascade classifier outside the loop for efficiency
facecascade = cv2.CascadeClassifier(harcascade)

while True:
    success, img = cap.read()
    if not success:
        break

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = facecascade.detectMultiScale(img_gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Face", img)  # Show the original image with rectangles

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture object and destroy all windows
cap.release()
cv2.destroyAllWindows()
