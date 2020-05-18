import cv2
import time
init = time.time()
cap = cv2.VideoCapture('rtsp://user:password@192.168.0.167/cam/realmonitor?channel=1&subtype=1') 
    
while True:
    _, frame = cap.read()
    

    print("contando",time.time()-init)
    cv2.imshow("frame", frame)
                
    key = cv2.waitKey(1)
    if time.time()-init>10:
        init = time.time()
        print("CAPTURADO")
        cv2.imwrite('capture/'+ str(time.time())+'.jpg', frame)
        print("************************************")
    if key == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()


