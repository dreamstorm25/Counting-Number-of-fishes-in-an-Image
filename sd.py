import cv2
import numpy as np
import os, os.path


fish_cascade  = cv2.CascadeClassifier('cascade.xml')
if not os.path.exists('results_610'):
    os.makedirs('results_610')

path = "C:/Users/Rishab/Documents/Flixsense/Dataset/fish_06"

#gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
i = 8627
tmp = 0 
for f in os.listdir(path):
    img = cv2.imread(os.path.join(path,f))
    #img = cv2.resize(img , (100,100))
    fish = fish_cascade.detectMultiScale(img)
    count = 0 ;
    p = ""
    for(x,y,w,h) in fish :
        if ( w > 35 ):
            if( h > 35 ) :
                count += 1
                cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
                tmp += 1
                p += str(x) + "_" + str(y) + "_"  + str(w) + "_"  + str(h)+ "_" 
    if(count > 0 ) :
        cv2.imwrite("results_610/" + str(i) + "_" + str(count) + "_" + p + ".jpg",img)
        i += 1 
    #if(count > 0):
     #   line = str(i)+ "_" + str(count) + "_" + str(p) + ".jpg " 
     #   line1 = str(count) + "_" + str(p)
     #   line = line + line1.replace("_"," ")
     #   cv2.imwrite("info/" + str(i)+ "_" + str(count) + "_" + str(p) + ".jpg",img)
     #   with open('info/annotations.lst','a') as h :
     #       h.write(line+'\n')
     #   i += 1
    

print(tmp)    

                 
