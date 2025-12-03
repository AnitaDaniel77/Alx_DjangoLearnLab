# Delete Book

```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()
# <QuerySet []>

---

## 📄 Final Summary File

Create:
```bash
nano CRUD_operations.md
# Django Shell CRUD Summary

Includes: create.md, retrieve.md, update.md, delete.md

Each file documents the Python commands and expected outputs for managing the Book model using Django ORM.
