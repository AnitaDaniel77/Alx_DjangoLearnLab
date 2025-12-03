from django.db import models

class Author(models.Model):
    # The Author model stores basic information about a writer.
    # Each Author can be linked to multiple Book instances (one-to-many relationship).
    name = models.CharField(max_length=100)

    def __str__(self):
        # This makes the admin and shell display the author's name instead of an ID.
        return self.name

class Book(models.Model):
    # The Book model stores details about a book.
    # Each Book is linked to one Author via a ForeignKey.
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        related_name='books',   # Allows reverse lookup: author.books.all()
        on_delete=models.CASCADE
    )

    def __str__(self):
        # This makes the admin and shell display the book title instead of an ID.
        return self.title


