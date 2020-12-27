from django.db import models
from django.contrib.auth.models import  User
from PIL import Image
from cloudinary.models import CloudinaryField

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile/')

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        # img = Image.open(self.image.path)

    def __str__(self):
        return f'{self.user.username} Profile'

# Create your models here.
