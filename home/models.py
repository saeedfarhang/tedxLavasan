from django.db import models

# models



# form options
class City(models.Model):
    title = models.CharField(max_length=56)
    
    def __str__(self):
        return self.title

# volunteer
class Degree(models.Model):
    title = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.title
 
# sponsor
class Participation(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

# speakers
class Activity(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

# site Forms
class IntroSpeaker(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=17 , blank=True)
    work = models.CharField(max_length=50)
    city = models.ForeignKey(City , on_delete=models.CASCADE,default={''})
    activity = models.ForeignKey(Activity,on_delete=models.CASCADE,null=True,blank=True)
    why = models.TextField()
    yourname = models.CharField(max_length=50)
    youremail = models.EmailField(max_length=254,blank=True)
    yourphone_number = models.CharField(max_length=17 , blank=True)

    def __str__(self):
        return self.name

class WorkWithUs(models.Model):
    name = models.CharField(max_length=56)
    email = models.EmailField()
    phone_number = models.CharField(max_length=17 , blank=True)
    degree = models.ForeignKey(Degree , on_delete = models.CASCADE,null=True)
    field = models.TextField()

    def __str__(self):
        return self.name

# sponsers

class Sponsor(models.Model):
    companyname = models.CharField(max_length=56)
    email = models.EmailField()
    phone_number = models.CharField(max_length=17 , blank=True)
    activity = models.CharField(max_length=100)
    participation = models.ForeignKey(Participation, on_delete = models.CASCADE, null=True)
    city = models.ForeignKey(City,on_delete= models.CASCADE, null=True)
    description = models.TextField()

    def __str__(self):
        return self.companyname