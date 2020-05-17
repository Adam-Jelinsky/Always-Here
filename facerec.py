import cv2
import face_recognition as fr
import numpy as np
import os

TOLERANCE = .5

NAMEPATH = "./facedata/names.txt"
namesfile = open(NAMEPATH,"r")
namesdata = namesfile.readlines()
names = []
facepaths = []
for i in range(len(namesdata)):
	if i % 2 == 1:
		facepaths.append(namesdata[i][0:-1])

def norm(ndarr):
	out = []
	for arr in ndarr:
		norm = 0
		for i in arr:
			norm = norm + i*i
		out.append(norm)
	return out


face_enc = []

for i in range(len(facepaths)):
	for enc in fr.face_encodings(fr.load_image_file(facepaths[i])):
		names.append(namesdata[2*i][0:-1])
		face_enc.append(enc)


print(face_enc)


uk_face_loc = []
uk_face_enc = []
process_this_frame = True

video_capture = cv2.VideoCapture(0)

while True:
	ret, frame = video_capture.read()
	small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

	# Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
	rgb_small_frame = small_frame[:, :, ::-1]

	if process_this_frame:
		uk_face_loc = fr.face_locations(rgb_small_frame)
		uk_face_enc = fr.face_encodings(rgb_small_frame, uk_face_loc)
		uk_face_names = []
		
		for enc in uk_face_enc:
			matches = fr.compare_faces(face_enc, enc, tolerance=TOLERANCE)
			name = "Unknown"
			face_dist = fr.face_distance(face_enc, enc)
			best_match_index = np.argmin(face_dist)
			if matches[best_match_index]:
				print(matches[best_match_index])
				name = names[best_match_index]
			uk_face_names.append(name)

	process_this_frame = not process_this_frame

	for (top, right, bottom, left), name in zip(uk_face_loc, uk_face_names):
		top *= 4
		right *= 4
		bottom *= 4
		left *= 4

		# Draw a box around the face
		cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

		# Draw a label with a name below the face
		cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
		font = cv2.FONT_HERSHEY_DUPLEX
		cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

	# Display the resulting image
	cv2.imshow('Video', frame)

	
	# Hit 'q' on the keyboard to quit!
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()





