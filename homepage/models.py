from django.db import models
from django.utils.text import slugify

class Adetails(models.Model):
    ip = models.TextField(default="")
    name = models.CharField(max_length=10,null=False)
    description = models.CharField(max_length=150,null=False)
    tags = models.CharField(max_length=500,null=False)
    hash_value = models.CharField(default=False,max_length=50,null=False)
    files = models.FileField(upload_to='')
    slug = models.SlugField(max_length=50)
    Report_vote = models.IntegerField(default=0)
    
    def get_unique_slug(self):
    # In this method a unique slug is created
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Adetails.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.get_unique_slug()
        super(Adetails,self).save(*args, **kwargs)


class Report_sound(models.Model):
    ip = models.TextField(default="")
    reason = models.TextField(default="")
    name = models.CharField(max_length=10,null=False)
    datetime = models.TextField(default="")
    hash_val = models.TextField(default="")
