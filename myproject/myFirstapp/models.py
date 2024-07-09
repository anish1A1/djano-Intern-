import datetime
import os
from django.db import models

# Create your models here.

def image_file_dir(request, filename):
    original_filename = filename
    time = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = time + original_filename  
    return os.path.join('image_uploads/', filename)  

class Blog(models.Model):
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length= 100)
    description = models.TextField(max_length=150)
    image = models.ImageField(upload_to=image_file_dir)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    #install pillow for ImageField

    