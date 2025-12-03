# LibraryProject
This is a basic Django project created for learning purposes.

# Task 1: Managing Permissions and Groups in Django

# Summary:
# - Added custom permissions to the Book model: can_view, can_create, can_edit, can_delete
# - Created user groups: Admins, Editors, Viewers
# - Used Django signals to automatically create groups and assign permissions after migrations
# - Connected signal logic using the ready() method in apps.py
# - Protected views using @permission_required decorators to enforce access control
# - Registered Book model in admin with clean list_display and list_filter settings
# - Tested group setup and permission enforcement using Django shell and admin panel

# Status:
# Task 1 is complete, tested, and ready for submission.

