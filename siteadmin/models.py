from django.db import models

# Create your models here.
class Speaker(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    intro = models.CharField(max_length=500)
    insta_id = models.CharField(max_length=100)
    long_description = models.TextField()
    site_address = models.CharField(max_length=100)
    image = models.ImageField(blank = True, default = 'user.png')

    def __str__(self):
        return self.name


class Team(models.Model):
    image = models.ImageField(blank = True, default = 'user.png')
    name = models.CharField(max_length=56)
    title = models.CharField(max_length=56)
    instagram = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name