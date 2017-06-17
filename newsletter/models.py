from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.


class SignUp(models.Model):
    user = models.ForeignKey(User, primary_key=True, on_delete=CASCADE)
    fullname = models.CharField(max_length=250, blank=False)
    bday = models.DateField(auto_now=False, auto_now_add=False)
    email = models.EmailField(max_length=254)
    profile_pic = models.FileField()
    background = models.FileField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.fullname

    def get_absolute_url(self):
        return reverse('update', kwargs={'pk': self.pk})



class Status(models.Model):
    status = models.CharField(max_length=1000)


    def get_absolute_url(self):
        return reverse('update', kwargs={'pk': self.pk})