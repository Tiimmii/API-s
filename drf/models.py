from django.db import models


# Create your models here.
class People(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name + " " + self.last_name

class Blog(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=2000)
    comment = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title