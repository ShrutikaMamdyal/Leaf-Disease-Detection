from django.db import models

# Create your models here.

class Leaf_Model(models.Model):
    leaf_id= models.AutoField
    leaf_image=models.ImageField(upload_to="Leaf_App/Images",default="",blank=True,null=True)
    
    
