from django.db import models

# Create your models here.


class Servidor(models.Model):
    name = models.CharField(max_length=200,null=False,default="")
    ipAddr = models.CharField(max_length=200,null=False)
    password = models.CharField(max_length=200,null=False,default="0")

    def __str__(self):
        return self.name
    