from django.db import models
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
# Create your models here.

class Movie(models.Model):
    hall = models.CharField(max_length = 150)
    movie = models.CharField(max_length = 150)
    
    def __str__(self):
        return self.movie

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

class Guest(models.Model):
    name = models.CharField(max_length = 150)
    mobile = models.CharField(max_length = 150)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Guest'
        verbose_name_plural = 'Guests'
        
class Reservation(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE , related_name='reservation_res')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE , related_name='reservation_res')
    
    def __str__(self):
        return self.guest.name

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE , blank=True , null=True)
    title = models.CharField(max_length = 150)
    body = models.TextField(max_length = 500)
    
    def __str__(self):
        return self.author.username

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def toketn_create(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)