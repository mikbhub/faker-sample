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

    _rating = (
        (1, "Bad"),
        (2, "Avarage"),
        (3, "Good"),
        (4, "Great"),
    )

    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField()
    rating = models.IntegerField(choices=_rating)
    
    def __repr__(self):
        return f"{self.__class__.__name__} {self.name} by {' '.join(str(a) for a in self.authors.all())} published by {self.publisher}"

    def __str__(self):
        return self.__repr__()


class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)

    def __repr__(self):
        return f"{self.__class__.__name__} {self.name}"

    def __str__(self):
        return self.__repr__()
