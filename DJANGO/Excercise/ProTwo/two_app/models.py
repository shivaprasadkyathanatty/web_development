from django.db import models

# Create your models here.
class Topic(models.Model):
    top_name=models.CharField(max_length=264,unique=True)
    def __str__(self):
        return self.top_name


class User(models.Model):
    first_name=models.CharField(max_length=264)
    last_name=models.CharField(max_length=264)
    email=models.EmailField()


class Webpage(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.PROTECT)
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)
    def __str__(self):
        return self.name



class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage,on_delete=models.PROTECT)
    date = models.DateField()
    def __str__(self):
        return str(self.date)
