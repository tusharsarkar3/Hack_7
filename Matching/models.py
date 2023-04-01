from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Questions(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    age=models.IntegerField()
    gender=models.CharField(max_length=2)

class Matches(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    matched_with = models.ForeignKey(User,related_name='matched_with_%(class)s_related',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    swiped_right = models.BooleanField(null=True, default=None)
    swiped_left = models.BooleanField(null=True, default=None)