from django.db import models

class Adetails(models.Model):
    name = models.CharField(max_length=10,null=False)
    desc = models.CharField(max_length=150,null=False)
    tags = models.CharField(max_length=500,null=False)
    hahv = models.CharField(default=False,max_length=50,null=False)
    files = models.FileField(upload_to='')
    

 