from django.db import models

class TodoItem(models.Model):
    # Fields for the TodoItem model
    title = models.CharField(max_length=255)  # Title of the to-do item
    description = models.TextField(blank=True, null=True)  # Optional description
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation
    completed = models.BooleanField(default=False)  # Completion status

    def __str__(self):
        return self.title
