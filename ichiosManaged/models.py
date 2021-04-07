from django.db import models

class statistics_oneword(models.Model):
    visiters = models.IntegerField(null=False,default=0)
    reports = models.IntegerField(null=False,default=0)
    upload = models.IntegerField(null=False,default=0)
    logs = models.IntegerField(null=False,default=0)

class logs(models.Model):
    l_loc = models.TextField()
    L_Description = models.TextField()
    l_datetime = models.TextField()

class recent(models.Model):
    ip = models.TextField()
    action =models.TextField()
    datetxt = models.TextField()
    timetxt =models.TextField()
    name = models.TextField()
    filepath = models.TextField()

class reports(models.Model):
    title = models.TextField()
    action =models.TextField()
    datetxt = models.TextField()
    timetxt =models.TextField()
    data = models.TextField()