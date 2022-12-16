import cv2 as cv
import numpy as np
house=np.zeros((800,1700,3),dtype='uint8')

house[:]=240, 240, 240

#For rectangle(Pillars of the house)
cv.rectangle(house,(250,400),(280,600),(255, 91, 77 ),thickness=cv.FILLED)
cv.rectangle(house,(480,400),(510,600),(255, 91, 77),thickness=cv.FILLED)
cv.rectangle(house,(715,180),(735,603),(255, 91, 77),thickness=cv.FILLED)
cv.rectangle(house,(720,10),(730,180),(205,92,92),thickness=cv.FILLED)
cv.rectangle(house,(940,400),(970,600),(255, 91, 77),thickness=cv.FILLED)
cv.rectangle(house,(1220,400),(1240,600),(255, 91, 77),thickness=cv.FILLED)
cv.rectangle(house,(1350,400),(1370,600),(255, 91, 77),thickness=cv.FILLED)
cv.rectangle(house,(744,219),(1390,600),(255, 91, 77),thickness=5)
cv.rectangle(house,(980,226),(1150,265),(255, 91, 77),thickness=2)
cv.rectangle(house,(300,458),(450,580),(255, 91, 77),thickness=2)

#Rectangle for national flag
cv.rectangle(house,(730,15),(850,45),(0, 0, 200),thickness=cv.FILLED )
cv.rectangle(house,(730,45),(850,75),(255,255,255),thickness=cv.FILLED)
cv.rectangle(house,(730,75),(850,105),(10, 100, 20),thickness=cv.FILLED)

#chakra
cv.circle(house,(790,59),13,(255,127,80),thickness=3)
#cv.line(house,(778,60),(802,60),(205,92,92),1)
#cv.line(house,(778,45),(802,75),(205,92,92),1)
#cv.line(house,(778,60),(802,60),(205,92,92),1)
#cv.line(house,(778,-190),(796,445),(205,92,92),1)


#Door for entry Gate
cv.rectangle(house,(512,405),(605,590),(102, 9, 0),thickness=cv.FILLED)
cv.rectangle(house,(609,405),(710,590),(102, 9, 0),thickness=cv.FILLED)

cv.rectangle(house,(972,405),(1095,590),(102, 9, 0),thickness=cv.FILLED)
cv.rectangle(house,(1099,405),(1215,590),(102, 9, 0),thickness=cv.FILLED)

#House boundary
cv.rectangle(house,(100,605),(1500,750),(60, 179, 113),thickness=cv.FILLED)


#Hinges for door
cv.circle(house,(592,500),10,(255, 232, 230),thickness=cv.FILLED)
cv.circle(house,(620,500),10,(255, 232, 230),thickness=cv.FILLED)

cv.circle(house,(1082,500),10,(2255, 232, 230),thickness=cv.FILLED)
cv.circle(house,(1110,500),10,(255, 232, 230),thickness=cv.FILLED)

#cv.circle(house,(375,505),20,(255,127,80),thickness=3)

cv.rectangle(house,(300,430),(450,580),(205,92,92),thickness=2)
cv.rectangle(house,(300,430),(450,580),(205,92,92),thickness=2)
cv.rectangle(house,(300,430),(450,580),(205,92,92),thickness=2)

#For rectangle(Roof for floor partitions of the house)
cv.rectangle(house,(235,390),(1390,398),(205,92,92),thickness=0)
cv.rectangle(house,(232,380),(710,390),(205,92,92),thickness=cv.FILLED)

#Rectangular Pillars for Night Lamps
#cv.rectangle(house,(125,200),(145,603),(255, 165, 0),thickness=2)

#cv.circle(house,(135,165),35,(60, 179, 113),thickness=5)
#cv.rectangle(house,(1465,200),(1485,603),(255, 165, 0),thickness=2)
#cv.circle(house,(1475,165),35,(60, 179, 113),thickness=5)

#For line(For triangular formation)
cv.line(house,(275,300),(650,300),(205,92,92),5)
cv.line(house,(235,380),(275,300),(205,92,92),5)
#cv.line(house,(750,380),(710,300),(205,92,92),5)

#Lines for Gym sheds
cv.line(house,(840,130),(900,210),(205,92,92),5)
cv.line(house,(900,130),(960,210),(205,92,92),5)
cv.line(house,(960,130),(1020,210),(205,92,92),5)
cv.line(house,(1020,130),(1080,210),(205,92,92),5)
cv.line(house,(1080,130),(1140,210),(205,92,92),5)
cv.line(house,(1140,130),(1200,210),(205,92,92),5)
cv.line(house,(1200,130),(1260,210),(205,92,92),5)
cv.line(house,(1260,130),(1320,210),(205,92,92),5)
cv.line(house,(1340,130),(1390,210),(205,92,92),5)
cv.line(house,(840,130),(740,210),(205,92,92),5)
cv.line(house,(840,130),(1340,130),(205,92,92),5)
cv.line(house,(745,212),(1390,212),(205,92,92),5)



#lines for house roof
cv.line(house,(280,300),(350,380),(205,92,92),5)
cv.line(house,(350,300),(410,380),(205,92,92),5)
cv.line(house,(410,300),(470,380),(205,92,92),5)
cv.line(house,(470,300),(530,380),(205,92,92),5)
cv.line(house,(530,300),(590,380),(205,92,92),5)
cv.line(house,(590,300),(650,380),(205,92,92),5)
cv.line(house,(650,300),(710,380),(205,92,92),5)



#cv.line(house,(275,300),(710,300),(205,92,92),5)
#cv.line(house,(275,300),(710,300),(205,92,92),5)
#cv.line(house,(275,300),(710,300),(205,92,92),5)
#cv.line(house,(275,300),(710,300),(205,92,92),5)

#For Circle
#cv.circle(blank,(250,250),40,(255,127,80),thickness=cv.FILLED)

#For line
#cv.line(blank,(250,250),(511,511),(255,0,0),5)

#Elipse
#cv.ellipse(house,(256,256),(100,50),0,0,180,255,-1)

#Polygon
#pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
#pts = pts.reshape((-1,1,2))
#cv.polylines(house,[pts],True,(0,255,255))

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(house,'',(50,50), font, 1,(184,134,11),2,cv.LINE_AA)

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(house,'KNOWLEDGE CENTRE',(985,254), font, 0.5,(220,20,60),1,cv.LINE_AA)

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(house,'ENQUIRY',(335,450), font, 0.5,(220,20,60),1,cv.LINE_AA)

cv.imshow('Canvas',house)
cv.waitKey(0)
cv.destroyAllWindows()