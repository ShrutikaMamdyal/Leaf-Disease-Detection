import cv2
import os
import numpy as np
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

new_model = load_model('./trained_model.h5')

print(new_model)

print("Model Loaded Successfully")

print("Models Summery")
new_model.summary()

leaf_image=cv2.imread("./Test Images/Early Blight/0c4f6f72-c7a2-42e1-9671-41ab3bf37fe7___RS_Early.B 6752.jpg")
test_image = cv2.resize(leaf_image, (256,256)) 


#CV2 reads an image in BGR format. We need to convert it to RGB
b,g,r = cv2.split(test_image)       # get b,g,r
rgb_img = cv2.merge([r,g,b])     # switch it to rgb

test_image = img_to_array(rgb_img)/255 # convert image to np array and normalize
test_image = np.expand_dims(rgb_img, axis = 0) # change dimention 3D to 4D


result = new_model.predict(test_image) # predict diseased palnt or not

print(result)

pred = np.argmax(result, axis=1) 



class_name=['Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy']
print("Predicted Disease:\t")
print(class_name[int(pred)])
confidence = np.max(result[0])
print("Confidence: " , (100*confidence))

