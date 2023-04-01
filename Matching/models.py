from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Questions(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    dob=models.CharField(max_length=20)
    tob=models.CharField(max_length=20)
    pob=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    age=models.IntegerField()
    partner_age_low=models.IntegerField()
    partner_age_high=models.IntegerField()
    gender=models.CharField(max_length=20)
    partner_gender=models.CharField(max_length=20)
    religion=models.CharField(max_length=20)
    partner_religion=models.CharField(max_length=20)
    mothertongue=models.CharField(max_length=20)
    partner_mothertongue=models.CharField(max_length=20)
    relationshiptype=models.CharField(max_length=20)
    edu=models.CharField(max_length=20)
    partner_edu=models.CharField(max_length=20)
    profession=models.CharField(max_length=20)
    partner_profession=models.CharField(max_length=20)
    datechar=models.CharField(max_length=20)
    animal=models.CharField(max_length=20)
    daynight=models.CharField(max_length=20)
    movie=models.CharField(max_length=20)
    music=models.CharField(max_length=20)
    minmax=models.CharField(max_length=20)
    EI=models.CharField(max_length=20)
    SN=models.CharField(max_length=20)
    TF=models.CharField(max_length=20)
    JP=models.CharField(max_length=20)
    interests=models.CharField(max_length=200)






class Matches(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    matched_with = models.ForeignKey(User,related_name='matched_with_%(class)s_related',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    swiped_right = models.BooleanField(null=True, default=None)
    swiped_left = models.BooleanField(null=True, default=None)