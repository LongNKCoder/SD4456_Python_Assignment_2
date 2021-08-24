from django.contrib.auth.models import User
from django.db import models

class Friendship(models.Model):
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    friend_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="friends")
