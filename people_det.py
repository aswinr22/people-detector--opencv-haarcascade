//created by Aswin R


import cv2
body_cascade=cv2.CascadeClassifier("C:/Users/pc/Desktop/haarcascade_fullbody.xml")
start_point=28,400
end_point=891,400
color=2550,0,0
thickness=2

def detect_body(frame):
	body=body_cascade.detectMultiScale(frame,1.15,4)
	for(x,y,w,h) in body:
		ox=cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
		print(ox)
		cv2.putText(ox,'People',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,0,0), 2)
		cv2.line(frame, (start_point),(end_point), (color),thickness) 
	return frame

def simulator():
	bodyvideo=cv2.VideoCapture("C:/Users/pc/Desktop/People.mp4")
	while bodyvideo.isOpened():
		
		ret,frame=bodyvideo.read()
		controlkey=cv2.waitKey(1)
		if ret:
			body_frame=detect_body(frame)
			cv2.imshow('frame',body_frame)
		
		else:
			break
		if controlkey==ord('q'):
			break
			

	bodyvideo.release()
	cv2.destroyAllWindows()

if __name__=='__main__':
	simulator()

