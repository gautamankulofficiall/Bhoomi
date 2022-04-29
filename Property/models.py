from django.db import models
from django.db.models.fields import CommaSeparatedIntegerField

# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class City(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    state = models.ForeignKey(to=State, on_delete=models.CASCADE)
    

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, unique=True)
    

    def __str__(self) -> str:
        return self.name


class Property(models.Model):
    category = models.ForeignKey(to=Category, related_name= "cat" ,on_delete=models.CASCADE)
    state = models.ForeignKey(to=State, related_name= "state" ,on_delete=models.CASCADE)
    city = models.ForeignKey(to=City, related_name= "city" ,on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class ContactUs(models.Model):
    username = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=15,blank=True,null=True,verbose_name=u"Phone number")
    message = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.username
