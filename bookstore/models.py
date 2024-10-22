from django.core.validators import MinValueValidator
from django.db import models


class Author(models.Model):
    id = models.AutoField(primary_key=True, unique=True, editable=False)

    first_name = models.CharField(max_length=100, unique=False, editable=True)
    last_name = models.CharField(max_length=100, unique=False, editable=True)


class Book(models.Model):
    id = models.AutoField(primary_key=True, unique=True, editable=False)

    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    title = models.CharField(max_length=150, unique=False, editable=True)
    count = models.PositiveIntegerField(validators=[MinValueValidator(0)], editable=True)

    def __str__(self):
        return "%s" % (self.title)
