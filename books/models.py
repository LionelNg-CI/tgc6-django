from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(blank=False, max_length=255)
    ISBN = models.CharField(blank=False, max_length=255)
    desc = models.TextField(blank=False)

    def __str__(self):
        return self.title


class Author(models.Model):
    First_Name = models.CharField(blank=False, max_length=255)
    Last_Name = models.CharField(blank=False, max_length=255)
    Date_of_Birth = models.DateField()

    def __str__(self):
        return self.First_Name
