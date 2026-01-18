from django.db import models

class Report(models.Model):
    CATEGORY_CHOICES = [
        ('traffic', 'Traffic'),
        ('road', 'Road Damage'),
        ('crime', 'Crime'),
    ]
    STATUS_CHOICES = [
        ('received', 'Received'),
        ('assigned', 'Assigned'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, blank=True)
    urgency = models.CharField(max_length=20, blank=True)
    credibility = models.FloatField(default=0)
    summary = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='received')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title