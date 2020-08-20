from django.db import models
from django.core.validators import RegexValidator


# models
class Speaker(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    intro = models.CharField(max_length=500)
    insta_id = models.CharField(max_length=100)
    long_description = models.CharField(max_length=1000)
    site_address = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# form options
class City(models.Model):
    title = models.CharField(max_length=56)
    
    def __str__(self):
        return self.title

class HowYouKnowUs(models.Model):
    title = models.CharField(max_length=500) 
    
    def __str__(self):
        return self.title

class Degree(models.Model):
    degree = models.CharField(max_length=50)

    def __str__(self):
        return self.degree

class Typeofparticipation(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

# site Forms
class IntroSpeaker(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_regix = RegexValidator(regex=r'^\+?1?\d(9,15)$')
    phone_number = models.CharField(validators=[phone_regix], max_length=17 , blank=True)
    work = models.CharField(max_length=50)
    city = models.ForeignKey(City , on_delete=models.CASCADE)
    typeofparticipation = models.ForeignKey(Typeofparticipation,on_delete=models.CASCADE)
    yourname = models.CharField(max_length=50)
    youremail = models.EmailField(max_length=254)
    phone_regix = RegexValidator(regex=r'^\+?1?\d(9,15)$')
    yourphone_number = models.CharField(validators=[phone_regix], max_length=17 , blank=True)


class WorkWithUs(models.Model):
    name = models.CharField(max_length=56)
    email = models.EmailField()
    phone_regix = RegexValidator(regex=r'^\+?1?\d(9,15)$')
    phone_number = models.CharField(validators=[phone_regix], max_length=17 , blank=True)
    degree = models.ForeignKey(Degree , on_delete = models.CASCADE,null=True)
    field = models.CharField(max_length=3000)

# sponsers

class Sponser(models.Model):
    companyname = models.CharField(max_length=56)
    email = models.EmailField()
    phone_regix = RegexValidator(regex=r'^\+?1?\d(9,15)$')
    phone_number = models.CharField(validators=[phone_regix], max_length=17 , blank=True)
    whatyoudo = models.CharField(max_length=50,null=True)
    typeofparticipation = models.ForeignKey(Typeofparticipation, on_delete = models.CASCADE, null=True)
    city = models.ForeignKey(City,on_delete= models.CASCADE, null=True)
    describtion = models.CharField(max_length=3000,null=True)
