import cv2
import numpy as np
face_classifier=cv2.CascadeClassifier('C:/Users/HP/Anaconda3/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
#now we need to extract the features of image which we will capture through camera
#------------image feature extractor
def face_extractor(img):
    #we convert the taken image which is in rbg into grayscale
    #cvtColor(img,scale into converter obj)
    img = np.full((100,80,3), 12, np.uint8)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_classifier.detectMultiScale(gray,1.3,5)
    #we got the image, now we have to check is there image or not 
    if faces is():#if faces is not there then
        return None 
    #if above condition is not satisfied then it means any face is detected so, now we crop the faces 
    for (x,y,w,h) in faces:
        cropped_face = img[y:y+h,x:x+w]#here cropping is done accoring to the size of image
    return cropped_face
#-------------camera configuration-----------------------------
cap=cv2.VideoCapture(0)#camera starts capturing 
count=0    #variables used to count the how many photos is taken 
while True:
    ret,frame=cap.read()#that line returns a frame which is captured
    if face_extractor(frame) is not None:#means if face is present
        count=count+1#increament the counter after capturing the picture
        #after detecting face in a captured image we have  to resize that image 
        faces=cv2.resize(face_extractor(frame),(200,200))#here resize the image first we have to detect the face so we get pass the frame as a parameter into the face_extractor, and to resize image means converting to a other measured value so here we too 300*300 pixles
        faces=cv2.cvtColor(faces,cv2.COLOR_BGR2GRAY)#converts the resized image into the grayscale
        #we have to give the name to resized image so we can save them in any specified location
        file_name_path="C:/Users/HP/Desktop/captures/alok"+str(count)+'.jpg'
        #save the image(here called variable faces) into the Location: file_name_path
        cv2.imwrite(file_name_path,faces)
        cv2.putText(faces,str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),4)
        #we want to show the cropped image so we use cv2.imshow(name_of_window,image)
        cv2.imshow('Face Cropper',faces)
    else:#that means simply face not found 
        print("face not found")
        pass#pass that message
    #------we need a condition where camera stop capturing shots so either ENTER(ASCII VALUE OF ENTER IS 13) get clicked or some maximum value of images 
    if cv2.waitKey(1)==13 or count==100:
        break
    #---------------we have to release the camera we doesn't it may create problem for our device 
cap.release()
    #----we have to close the windows and deallocate any associated memory usage
cv2.destroyAllWindows()
#end of collecting the data
print("Collecting the IMAGES completed :)")
#----------------------------------end of program-------------------------    