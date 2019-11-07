from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __repr__(self):
        return f"{self.__class__.__name__} {self.name} {self.age}"

    def __str__(self):
        return self.__repr__()


class Publisher(models.Model):
    name = models.CharField(max_length=300)

    def __repr__(self):
        return f"{self.__class__.__name__} {self.name}"

    def __str__(self):
        return self.__repr__()


class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField()

    def __repr__(self):
        return f"{self.__class__.__name__} {self.name} by {' '.join(self.authors)} published by {self.publisher}"

    def __str__(self):
        return self.__repr__()


class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)

    def __repr__(self):
        return f"{self.__class__.__name__} {self.name}"

    def __str__(self):
        return self.__repr__()
