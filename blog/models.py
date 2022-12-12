from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User # proides the users registered


# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})
    

class Comments(models.Model):
    author = models.CharField(max_length=15)
    comments = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Posts', on_delete= models.CASCADE)
