from django.db import models

# Create your models here.
#The below code is copy pasted from google and then altered.

class Contact(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    gender = models.CharField(max_length=7)
    desc = models.TextField()

    #By adding the following method we can display the content in the name of the object on the admin page.
    def __str__(self):
        return self.name +" - "+self.email