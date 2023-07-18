from django.db import models

# About Models
class About(models.Model):
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='About')

    class Meta:
        verbose_name = "About me"
        verbose_name_plural = "About me"

    def __str__(self):
        return "About me"
    

# Service Model
class Service(models.Model):
    name = models.CharField(max_length=100,verbose_name="service name")
    description = models.TextField(verbose_name="About Service")

    def __str__(self):
        return self.name
    

# Recent Work Model
class Recent_Work(models.Model):
    title = models.CharField(max_length=100,verbose_name="work title")
    image = models.ImageField(upload_to="works")

    def __str__(self):
        return self.title
    

# Client Model
class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="client name")
    description = models.TextField(verbose_name="client say")
    image = models.ImageField(upload_to="clients", default="default.png")

    def __str__(self):
        return self.name