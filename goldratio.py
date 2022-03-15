#Notes:

#(0,0) is upper left corner

#distance from the top of the nose to the centre of the lips should be 1.618 times the distance
#from the centre of the lips to the chin
#---> top of nose is the 1st point, centre of lips is the half-way point of the y-component of the 10th point, bottom of chin is the 9th point


#the hairline to the upper eyelid should be 1.618 times the length of the top of the upper eyebrow
#to the lower eyelid
#---> hairline??????????????

#the ideal ratio of upper to lower lip volume is 1:1.6 (the lower lip should have slightly more 
#volume than the upper lip
#---> lip volume????????

#length of your face divided by the width of your face
#---> width can be taken at the cheekbones (2nd point)

#width of lips divided by the length and length of nose divided by the width 
#---> upper: length = 7th point - 1st point on x-axis; width = 4th point - 10th point on y-axis
#---> lower: length = 1st point - 7th point on x - axis; width = 4th point - 10th point on y-axis

#the area from the eye to the eyebrow divided by the area of the eyebrow
#---->????

#width of the chin just below the lip should be 1.618 the length of the lip
#-----> width of chin = 13th point - 5th point on x-axis
#---> length of lip = 1st point - 7th point on x-axis

#NOSE: (nose length divided by nose width)/1.618 = percentage score of nose Phi ratio
#if nose ratio smaller than PHi
#---> nose length = all 5 points on y-axis of nose bridge
#---> nose width = 5th point of nose tip minus 1st point on x-axis

#EYEBROWS: measure your eyebrow from the end nearest to your nose to the arch in a straight line
# = Arch Length
#---> use pythagorean theorem
#measure eyebrow from the same end to the opposite tip in a straight line = full length
#---> use pythagorean theorem
#divide full length by arch length = eyebrow ratio

#LIPS: measure the length of the lip from end to end = Lip Length
#Divide Lip Length by Nose Width
#the distance from the corner of the lip to the opposite edge of the nose should also be 
#---> use pythagorean theorem
#equal to Base of Nose * 1.618

#length and width of the face, then divide length by width, result should be 1.6
#---> 2nd point of chin, 16th point are width; 

#from the forehead hairline to a spot between the eyes, from between the eyes to the bottom
#of the nose, and from the bottom of the nose to the bottom of the chin, numbers should be equal
#---> hairline = ????
#---> 1st nose point to last nose point
#---> from last nose point to 9th nose point   all y-axis

#length of an ear is equal to the length of the nose, and the width of an eye is equal to the 
#distance between eyes
#--->length of ear???
#---> 1st point and 4th point = width of an eye x-axis
#---> 4th point of right eye and 1st point of left eye x-axis

#distance between eyes divided by the length of the eye should equal phi
#---> 1st point and 4th point = width of an eye x-axis
#---> 4th point of right eye and 1st point of left eye x-axis

#distance from the nose to the edge of the eye, divided by the distance from the edge of the eye 
#to the corner of the lips should equal phi

#the area of the bottom lip divided by the area of top lip should equal phi
#the length of the lip end to end divided by the distance at the base of the nose = phi
#corner of lip to opposite corner of nose, divided by length of the base of the nose = phi

#the area from the eye to the eyebrow divided by the area of the eyebrow

from PIL import Image, ImageDraw
import face_recognition
import scipy.constants
import numpy as np

photo="test12.png"    #enter name of file here

print("Welcome to the facial beauty calculator. This program will perform various calculations on the face in any image you provide based on calculations performed on the face of many beauty models and compare the results to the golden ratio. Please, provide images where the entire face is included. The face in the image should be expressionless and relaxed for best results. Any expressions may change the results.")
print("Results are provided for some individual landmarks and properties of the face. Then a total beauty score is calculated.")
print("Additionally, a comparison between the photo of the face and the computationally generated perfect face is calculated. This comparison is independent of the first measurements.")
print("Please, enjoy!")
# Load the jpg file into a numpy array
image = face_recognition.load_image_file(photo)

# Find all facial features in ll the faces in the image
face_landmarks_list = face_recognition.face_landmarks(image)  #(0,0) is upper left corner

if (len(face_landmarks_list))>1:
   print("Sorry, there are too many faces in the image. Only use image of one face.")
elif (len(face_landmarks_list))==0:
   print("Sorry, no image was detected in the image. Please, try again.")

#print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))

# Create a PIL imagedraw object so we can draw on the picture
pil_image = Image.fromarray(image)
d = ImageDraw.Draw(pil_image)

nose_top=[]

#extraction of coordinates
lists=[]
   
for face_landmarks in face_landmarks_list:

    # Print the location of each facial feature in this image
    for facial_feature in face_landmarks.keys():
        #print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))
        lists.append(face_landmarks[facial_feature])  #first list is chin, 2nd list is left eyebrow, 3rd is right eyebrow, 4th is nose bridge, 5th is nose tip, 6th is left eye, 7th is right eye, 8th is top lip, 9th is bottom lip
    n=0
    # Let's trace out each facial feature in the image with a line!
    for facial_feature in face_landmarks.keys():
        n=n+1
        m=str(n)
        d.point(face_landmarks[facial_feature])

# Show the picture
pil_image.show()

chin=[]
left_eyebrow=[]
right_eyebrow=[]
nose_bridge=[]
nose_tip=[]
left_eye=[]
right_eye=[]
top_lip=[]
bottom_lip=[]

chin.append(lists[0])
left_eyebrow.append(lists[1])
right_eyebrow.append(lists[2])
nose_bridge.append(lists[3])
nose_tip.append(lists[4])
left_eye.append(lists[5])
right_eye.append(lists[6])
top_lip.append(lists[7])
bottom_lip.append(lists[8])

##distance from the top of the nose to the centre of the lips should be 1.618 times the distance
#from the centre of the lips to the chin
#---> top of nose is the 1st point, centre of lips is the half-way point of the y-component of the 10th point, bottom of chin is the 9th point
(x1,y1)=nose_bridge[0][0]
(x2,y2)=top_lip[0][9]
(x3,y3)=bottom_lip[0][9]
(x4,y4)=chin[0][8]
a=(((y2+y3)/2)-y1)
b=((y4-((y2+y3)/2)))
value1=((b/a)/(scipy.constants.golden))*100  #(should equal scipy.constants.golden)

#length of your face divided by the width of your face
#---> width can be taken at the cheekbones (1st point and 17th point), length can be taken 1st point of chin and 9th point of chin
(x1,y1)=chin[0][0]
(x2,y2)=chin[0][16]
(x3,y3)=chin[0][8]
a=x2-x1
b=y3-y1
value2=((b/a)/scipy.constants.golden)*100


#NOSE: (nose length divided by nose width)/1.618 = percentage score of nose Phi ratio
#if nose ratio smaller than PHi
#---> nose length = all 5 points on y-axis of nose bridge
#---> nose width = 5th point of nose tip minus 1st point on x-axis
(x1,y1)=nose_bridge[0][3]
(x2,y2)=nose_tip[0][4]
value3=((y1/x2)/(scipy.constants.golden))*100
print("The beauty ratio of your nose is",value3,"%")

#EYEBROWS: measure your eyebrow from the end nearest to your nose to the arch in a straight line
# = Arch Length
#---> use pythagorean theorem, 3rd point, and 5th point
(x1,y1)=left_eyebrow[0][2]
(x2,y2)=left_eyebrow[0][4]
(x3,y3)=right_eyebrow[0][0]
(x4,y4)=right_eyebrow[0][2]
a1=x2-x1
b1=y1-y2
a2=x4-x3
b2=y3-y4
result1=np.sqrt((a1**2)+(b1**2))
result2=np.sqrt((a2**2)+(b2**2))
#measure eyebrow from the same end to the opposite tip in a straight line = full length
#---> use pythagorean theorem
(x1,y1)=left_eyebrow[0][0]
(x2,y2)=left_eyebrow[0][4]
(x3,y3)=right_eyebrow[0][0]
(x4,y4)=right_eyebrow[0][4]
a1=x2-x1
b1=y1-y2
a2=x4-x3
b2=y4-y3
result3=np.sqrt((a1**2)+(b1**2))
result4=np.sqrt((a2**2)+(b2**2))
#divide full length by arch length = eyebrow ratio ---> arch length/full length since arch length is always lower than full length
value4=((result1/result3)/(scipy.constants.golden))*100    #left eyebrow
value5=((result2/result4)/(scipy.constants.golden))*100    #right eyebrow
print("The beauty ratio of your right eyebrow is",value4,"%")
print("The beauty ratio of your left eyebrow is",value5,"%")

#LIPS: measure the length of the lip from end to end = Lip Length
#Divide Lip Length by Nose Width
(x1,y1)=top_lip[0][0]
(x2,y2)=bottom_lip[0][0]
(x3,y3)=nose_tip[0][0]
(x4,y4)=nose_tip[0][4]
a1=x2-x1
b1=x4-x3
value6=((b1/a1)/(scipy.constants.golden))*100       #not included in final measurement
print("The beauty ratio of your lips is",value6,"%")


#the distance from the corner of the lip to the opposite edge of the nose should also be 
#---> use pythagorean theorem
#equal to Base of Nose * 1.618
(x1,y1)=top_lip[0][0]
(x2,y2)=nose_tip[0][4]
(x3,y3)=bottom_lip[0][0]
(x4,y4)=nose_tip[0][0]
a1=x2-x1
b1=y1-y2
a2=x3-x4
b2=y3-y4
c1=x2-x4
result1=np.sqrt((a1**2)+(b1**2))
result2=np.sqrt((a2**2)+(b2**2))
value7=((c1/result1)/(scipy.constants.golden))*100
value8=((c1/result2)/(scipy.constants.golden))*100

#from the forehead hairline to a spot between the eyes, from between the eyes to the bottom
#of the nose, and from the bottom of the nose to the bottom of the chin, numbers should be equal
#---> hairline = ????
#---> 1st nose point to last nose point
#---> from last nose point to 9th nose point   all y-axis
#(x1,y1)=nose_bridge[0][0]
#(x2,y2)=nose_tip[0][2]
#(x3,y2)=chin[0][8]
#result1=y2-y1
#result2=y3-y2
#value20=(result1-result2)


#length of an ear is equal to the length of the nose, and the width of an eye is equal to the 
#distance between eyes
#--->length of ear???
#---> 1st point and 4th point = width of an eye x-axis
#---> 4th point of right eye and 1st point of left eye x-axis
(x1,y1)=left_eye[0][0]
(x2,y2)=left_eye[0][3]
(x3,y3)=right_eye[0][0]
(x4,y4)=right_eye[0][3]
a1=x2-x1
b1=x4-x3
c1=x3-x2
#result1=c1-a1
#result2=c1-b1

#distance between eyes divided by the length of the eye should equal phi
#---> 1st point and 4th point = width of an eye x-axis
#---> 4th point of right eye and 1st point of left eye x-axis
value9=((a1/c1)/(scipy.constants.golden))*100  #left eye
value10=((b1/c1)/(scipy.constants.golden))*100  #right eye
print("The beauty ratio of your right eye is",value9,"%")
print("The beauty ratio of your left eye is",value10,"%")

#distance from the nose to the edge of the eye, divided by the distance from the edge of the eye 
#to the corner of the lips should equal phi
(x1,y1)=nose_tip[0][2]
(x2,y2)=right_eye[0][3]
(x3,y3)=bottom_lip[0][0]
(x4,y4)=top_lip[0][0]
(x5,y5)=left_eye[0][0]
a1=x2-x1
b1=y1-y2
result1=np.sqrt((a1**2)+(b1**2))
a2=x2-x3
b2=y3-y2
result2=np.sqrt((a2**2)+(b2**2))
a3=x1-x5
b3=y1-y5
result3=np.sqrt((a3**2)+(b3**2))
a4=x4-x5
b4=y4-y5
result4=np.sqrt((a4**2)+(b4**2))
value11=((result1/result2)/(scipy.constants.golden))*100
value12=((result3/result4)/(scipy.constants.golden))*100
#width of lips divided by the length and length of nose divided by the width 
#---> upper: length = 7th point - 1st point on x-axis; width = 4th point - 10th point on y-axis
#---> lower: length = 1st point - 7th point on x - axis; width = 4th point - 10th point on y-axis
#length
(x1,y1)=top_lip[0][0]
(x2,y2)=top_lip[0][6]
(x3,y3)=bottom_lip[0][6]
(x4,y4)=bottom_lip[0][0]
#width
(x5,y5)=top_lip[0][3]
(x6,y6)=top_lip[0][9]
(x7,y7)=bottom_lip[0][3]
(x8,y8)=bottom_lip[0][9]
a1=x2-x1
b1=y6-y5
value13=((b1/a1)/(scipy.constants.golden))*100           #unused measurements
a2=x4-x3
b2=y7-y8
value14=((b1/a1)/(scipy.constants.golden))*100      #unused value

(x9,y9)=nose_tip[0][2]
(x10,y10)=nose_bridge[0][0]
(x11,y11)=nose_tip[0][0]
(x12,y12)=nose_tip[0][4]
a1=y9-y10
b1=x12-x11
value15=((b1/a1)/(scipy.constants.golden))*100    #unused value

#width of the chin just below the lip should be 1.618 the length of the lip
#-----> width of chin = 13th point - 5th point on x-axis
#---> length of lip = 1st point - 7th point on x-axis
(x1,y1)=chin[0][7]
(x2,y2)=chin[0][9]
a1=x2-x1
(x3,y3)=bottom_lip[0][6]
(x4,y4)=bottom_lip[0][0]
b1=x4-x3
value16=((a1/b1)/(scipy.constants.golden))*100

#while calculating the final beauty rating, eyebrows and eyes are considered as one value and not split into right and left, since ratings that include forehead and ears are missing additional points have been removed (a total of 400 points), also the corner of lip/nose ratio is considered to be one, value11 and value12 count as one, value9 and value10 considered as one
finalvalue=((value1+value2+value3+value4+value5+value6+value7+value8+value9+value10+value11+value12+value16)/600)*100
print("Congradulations! Your total beauty score is",finalvalue,"%")


# Often instead of just checking if two faces match or not (True or False), it's helpful to see how similar they are.
# You can do that by using the face_distance function.

# The model was trained in a way that faces with a distance of 0.6 or less should be a match. But if you want to
# be more strict, you can look for a smaller face distance. For example, using a 0.55 cutoff would reduce false
# positive matches at the risk of more false negatives.

# Note: This isn't exactly the same as a "percent match". The scale isn't linear. But you can assume that images with a
# smaller distance are more similar to each other than ones with a larger distance.

# Load some images to compare against
known_obama_image = face_recognition.load_image_file("mask3.jpg")
#known_biden_image = face_recognition.load_image_file("test.jpg")

# Get the face encodings for the known images
obama_face_encoding = face_recognition.face_encodings(known_obama_image)[0]
#biden_face_encoding = face_recognition.face_encodings(known_biden_image)[0]

known_encodings = [
    obama_face_encoding,
    #biden_face_encoding
]

# Load a test image and get encondings for it
image_to_test = face_recognition.load_image_file(photo)
image_to_test_encoding = face_recognition.face_encodings(image_to_test)[0]

# See how far apart the test image is from the known faces
face_distances = face_recognition.face_distance(known_encodings, image_to_test_encoding)

for i, face_distance in enumerate(face_distances):
    print("Your face is {:.3}% different from the perfect face!".format(face_distance*100))
    #print("- With a normal cutoff of 0.6, would the test image match the known image? {}".format(face_distance < 0.6))
    #print("- With a very strict cutoff of 0.5, would the test image match the known image? {}".format(face_distance < 0.5))
    #print()


#References:
#https://www.dailymail.co.uk/femail/article-3691691/Are-beautiful-Amber-Heard-Face-mapping-expert-puts-FEMAIL-s-faces-test-compare-perfect-listers-surprising-results.html
#https://www.medisculpt.co.za/golden-ratio-beautiful-face/
#https://www.oprah.com/oprahshow/measuring-facial-perfection-the-golden-ratio
