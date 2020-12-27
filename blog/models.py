from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import  Image
from cloudinary.models import CloudinaryField
# Create your models here
class Post(models.Model):
    title=models.CharField(max_length=150)
    image=models.ImageField(upload_to='posts/')
    # content= models.TextField(blank=True,null=True)
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return  str(self.author.username)

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})

