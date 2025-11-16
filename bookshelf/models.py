from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100, default="Unknown")
    publication_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title




from django.db import models

class Placeholder(models.Model):
    name = models.CharField(max_length=100)
