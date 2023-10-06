from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length=100)
    content= models.TextField()
    date_posted= models.DateTimeField(default=timezone.now)
    author= models.ForeignKey(User, on_delete= models.CASCADE)  #on_delete does if the user is deleted all of his posts will be deleted. But if you delete the psot the user will not be deleted

    def __str__(self):
        return self.title
    