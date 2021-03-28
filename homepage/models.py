from django.db import models

class Adetails(models.Model):
    ip = models.TextField(default="")
    name = models.CharField(max_length=10,null=False)
    description = models.CharField(max_length=150,null=False)
    tags = models.CharField(max_length=500,null=False)
    hash_value = models.CharField(default=False,max_length=50,null=False)
    files = models.FileField(upload_to='')