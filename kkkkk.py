import face_recognition
import cv2
import pickle

data = pickle.loads(open("kartik.pickle", "rb").read())
print("Importing pickled data")
print(data)

face_locations = []
face_encodings = []
face_names = []

cap = cv2.VideoCapture(0)
pk = True

while True:

    ret, frame = cap.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    if pk:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []

        for encoding in encodings:
            matches = face_recognition.compare_faces(data["encodings"], encoding)
            if True in matches:
 
                matched = [i for (i, b) in enumerate(matches) if b]
                for i in matched:

                    name = data["names"][i]
                    face_names.append(name)


              
    pk = not pk
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 255), 2)

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (0, 255, 255), 1)

    
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;

cap.release()
cv2.destroyAllWindows()
