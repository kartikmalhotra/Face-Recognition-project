
import face_recognition
import pickle
import cv2
import os

knownEncodings = []
knownNames = []



path = "K:\\prog"
for root, dirs, files in os.walk(path):
     for name in files:    
            if name.endswith(".jpg"):
                print (name)
                l = os.path.basename(root)
                print(l)
                image = cv2.imread(os.path.join(root, name))
                rgb_small_frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                boxes = face_recognition.face_locations(rgb_small_frame)
                encodings = face_recognition.face_encodings(rgb_small_frame, boxes)
                for encoding in encodings:
                  knownEncodings.append(encoding)
                  knownNames.append(l)

# dump the facial encodings + names to disk
print("Save the encodings")
data = {"encodings": knownEncodings, "names": knownNames}
f = open("kartik.pickle", "wb")
f.write(pickle.dumps(data))
f.close()
