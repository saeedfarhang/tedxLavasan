from django.db import models
from django.core.validators import RegexValidator



class City(models.Model):
    title = models.CharField(max_length=56)
    
    def __str__(self):
        return self.title

class HowYouKnowUs(models.Model):
    title = models.CharField(max_length=500) 
    
    def __str__(self):
        return self.title

class Signup(models.Model):
    name = models.CharField(max_length=56)
    email = models.EmailField(max_length=254 , help_text='enter your email')
    phone_regix = RegexValidator(regex=r'^\+?1?\d(9,15)$')
    phone_number = models.CharField(validators=[phone_regix], max_length=17 , blank=True)
    city = models.ForeignKey(City , on_delete=models.CASCADE)
    howyouknowus = models.ForeignKey(HowYouKnowUs , on_delete = models.CASCADE, null=True)
    tedxExperience = models.BooleanField(null=True)
    

    def __str__(self):
        return self.name
    
class Degree(models.Model):
    degree = models.CharField(max_length=50)

class WorkWithUs(models.Model):
    name = models.CharField(max_length=56)
    email = models.EmailField()
    phone_regix = RegexValidator(regex=r'^\+?1?\d(9,15)$')
    phone_number = models.CharField(validators=[phone_regix], max_length=17 , blank=True)
    degree = models.ForeignKey(Degree , on_delete = models.CASCADE,null=True)
    field = models.CharField(max_length=3000)

# sponsers
class Typeofparticipation(models.Model):
    title = models.CharField(max_length=100)

class Sponser(models.Model):
    companyname = models.CharField(max_length=56)
    email = models.EmailField()
    phone_regix = RegexValidator(regex=r'^\+?1?\d(9,15)$')
    phone_number = models.CharField(validators=[phone_regix], max_length=17 , blank=True)
    whatyoudo = models.CharField(max_length=50,null=True)
    typeofparticipation = models.ForeignKey(Typeofparticipation, on_delete = models.CASCADE, null=True)
    city = models.ForeignKey(City,on_delete= models.CASCADE, null=True)
    describtion = models.CharField(max_length=3000,null=True)
