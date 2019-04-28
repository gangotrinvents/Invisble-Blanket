import numpy as np
import cv2
ref=cv2.imread(r"C:\Users\ashum\OneDrive\Desktop\pp.jpg")
ref=cv2.resize(ref,(640,480))
def show_webcam(mirror=False):
    cap=cv2.VideoCapture(0)
    while True:
        _,frame=cap.read()
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        lower=np.array([0,0,0])      #lower=np.array([150,150,50])
        upper=np.array([0,255,255])     #upper=np.array([180,255,150])
        mask=cv2.inRange(hsv,lower,upper)
        mask2=cv2.bitwise_not(mask)
        cv2.imshow("magic",mask)
        #print("mask",mask.shape)
        #print("ref",ref.shpe)
        cv2.imshow("ref",ref)
        s=cv2.bitwise_and(ref,ref,mask=mask)
        s2=cv2.bitwise_and(frame,frame,mask=mask2)
        a=cv2.add(s,s2)
        cv2.imshow("magic",a)
        if cv2.waitKey(1) == 27: 
            break
cv2.destroyAllWindows()

def main():
    show_webcam(mirror=True)


if __name__ == '__main__':
    main()


    
