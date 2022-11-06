import datetime

from django.db import models
from django.utils import timezone


class NewUsers(models.Model):
    username = models.TextField()
    password = models.TextField()
    id = models.BigAutoField(primary_key=True)

# FIX Cryptographic Failures:
#    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Texts(models.Model):
    owner = models.ForeignKey(NewUsers, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.content

