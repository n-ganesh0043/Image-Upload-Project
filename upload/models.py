from django.db import models

# Create your models here.
class Imageupload(models.Model):
    img_upload=models.ImageField(upload_to='product_images/')
    name=models.CharField(max_length=20,default=False)