class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]
