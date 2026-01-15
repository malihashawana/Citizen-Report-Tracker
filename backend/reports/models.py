from django.db import models

class Report(models.Model):
    CATEGORY_CHOICES = [
        ('traffic', 'Traffic'),
        ('road', 'Road Damage'),
        ('crime', 'Crime'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
