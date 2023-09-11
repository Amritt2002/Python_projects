import cv2
face_cap = cv2.CascadeClassifier("C:/Users/AMRITANSHU//AppData/Roaming/Python/Python311/site-packages/cv2/data"
                                 "/haarcascade_frontalface_default.xml")
video_cap = cv2.VideoCapture(0)

if not video_cap.isOpened():
    print("Error: Could not open video capture.")
    exit()

while True:
    ret, video_data = video_cap.read()
    col = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
    faces = face_cap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    for(x, y, w, h) in faces:
        cv2.rectangle(video_data, (x, y), (x+w, y+h), (0, 255, 0), 2)

    if not ret:
        print("Error: Failed to read a frame from the camera.")
        break

    cv2.imshow("video_live", video_data)

    if cv2.waitKey(100) == ord("a"):
        break

video_cap.release()
cv2.destroyAllWindows()
