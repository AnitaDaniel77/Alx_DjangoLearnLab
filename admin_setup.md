# Django Admin Configuration for Book Model

## Admin Registration
Registered the `Book` model using `@admin.register(Book)`.

## Custom Display
- `list_display`: Shows title, author, and publication_year in the list view.
- `list_filter`: Enables filtering by author and publication_year.
- `search_fields`: Allows searching by title and author.

## Access
Visit `/admin` and log in with superuser credentials to manage books.
