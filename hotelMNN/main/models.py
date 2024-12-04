# main/models.py
from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Отзыв от {self.name}"
