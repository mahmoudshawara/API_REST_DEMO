from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField()
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    author = models.ForeignKey(Author,on_delete=models.DO_NOTHING)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    def __str_(self):
        return self.title
