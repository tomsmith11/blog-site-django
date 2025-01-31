from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  # Import Django's User

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title} by {self.author}"