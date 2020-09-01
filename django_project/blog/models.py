from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse 

class Post(models.Model):
    title=models.CharField(max_length=100)
    date_of_post=models.DateTimeField(default=timezone.now)
    content=models.TextField()
    author=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    # redirect will actually redirect you to a specific route
    # whereas reverse will return the full url to that route as a string 
    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk': self.pk})