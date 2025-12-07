from django.db import models

# Author model represents a book author with a name field
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name  # Return author name when printed


# Book model represents a book with title, publication year, and linked author
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    # ForeignKey creates a one-to-many relationship: one author can have many books
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

