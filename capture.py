import cv2

cap = cv2.VideoCapture(0)

while True:
    #capture frame
    ret, frame = cap.read()
    
    #Display frame 
    cv2.imshow('frame', frame)    
    
    #when 'ESC' key done, finish loop process
    if cv2.waitKey(1) == 27:
        break
    
cap.release()
cv2.destroyAllWindows()