from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

# Code was adapted and inspired by the lectures from Dr Scharlau at the University of Aberdeen - in the 'Enterprise Software Development' module.
# switch customer to user so that we can use Django's componenents
# https://blog.crunchydata.com/blog/extending-djangos-user-model-with-onetoonefield 
# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    address = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.email}, {self.customer.address}'

    class Meta:
        db_table = 'customer'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Customer.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.customer.save()

class Song(models.Model):
    songID = models.CharField(max_length=30, default="SOME ID")
    songName = models.TextField()
    songAuthor = models.TextField()
    songVolume = models.TextField(default="SOME VOLUME")
    songGenre = models.TextField(default="SOME GENRE")
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images')


    def __str__(self):
        return f'{self.songID},{self.songName},{self.songAuthor},{self.description},{self.created_date},{self.image},{self.songVolume},{self.songGenre}'

class SongImage(models.Model):
    song = models.ForeignKey(Song, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return str(self.song.id)
