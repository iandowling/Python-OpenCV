import cv2
import sys

cascadeFile = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascadeFile)

camera = cv2.VideoCapture(0)

while True :
        #return frame-by-frame
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        facedetect = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
        )

        #Draw a rectangle around faces
        for (x, y, w, h) in facedetect:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        #Display the result
        cv2.imshow('Video', frame)

        if not cv2.GrabFrame(camera):
                break

        frame = cv2.RetrieveFrame(camera)
        sys.stdou.write(frame.tostring())

        if cv2.waitKey(1) & 0xFF == ord('q'):
                break

camera.release()
cv2.destroyAllWindows()

