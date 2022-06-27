from asyncio.windows_events import NULL
from gettext import NullTranslations
from tkinter import Image
from django.http import HttpResponse
from django.shortcuts import render,redirect
import numpy as np
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from .models import Leaf_Model
from PIL import Image
import base64



def Home(request):
    if request.method=="POST":
        demo_model= Leaf_Model() #to access Uploaded image from model
        demo_model.leaf_image=request.FILES['myfile']  #getting image 
        b64_img = base64.b64encode(demo_model.leaf_image.file.read()).decode('ascii') # converting it to base64 for url
        demo_model.save()
        CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]
        loaded_model=load_model('./trained_model.h5') # loading my model tensorflow
        image=Image.open(demo_model.leaf_image) #PIL
        img_batch = np.expand_dims(image, 0) #Dim changing
        predictions = loaded_model.predict(img_batch) # Predicting
        predicted_class = CLASS_NAMES[np.argmax(predictions[0])] # Result
        print(predicted_class)
        confidence = np.max(predictions[0])*100 # accuracy
        print(confidence) 
        res = "{:.2f}".format(confidence)
        demo_model.clean()
        return render(request, "Leaf_App/Result_Page.html", {'result': predicted_class, 'accuracy': res,'file_url':b64_img})   
    return render(request,"Leaf_App/Home_Page.html")

def Result(request):
    return render(request,"Leaf_App/Result_Page.html")

def Help(request):
    return render(request,"Leaf_App/Help_Page.html")