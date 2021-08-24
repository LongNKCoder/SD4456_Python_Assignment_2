from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    privacy_choices = [
        ("Pub", "Public"),
        ("Pri", "Private"),
        ("On", "Only you"),
    ]
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    privacy = models.CharField(max_length=3, choices=privacy_choices, null=False)
    date_post = models.DateField(auto_now=True)
