from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_year')
    list_filter = ('publication_year',)

admin.site.register(Book, BookAdmin)

