from django.db import models


# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return self.first_name + self.last_name + self.email


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    # publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()


class Message(models.Model):
    title = models.CharField(max_length=100)
    keyword = models.CharField(max_length=200)
    content = models.CharField(max_length=300)
    publication_date = models.DateField()
    addItem = models.CharField(max_length=400, default="000")
