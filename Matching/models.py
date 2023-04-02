from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.utils import timezone

class Questions(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    dob=models.CharField(max_length=20, null=True)
    tob=models.CharField(max_length=20, null=True)
    pob=models.CharField(max_length=20, null=True)
    state=models.CharField(max_length=20, null=True)
    city=models.CharField(max_length=20, null=True)
    age=models.IntegerField(null=True)
    partner_age_low=models.IntegerField(null=True)
    partner_age_high=models.IntegerField(null=True)
    gender=models.CharField(max_length=20, null=True)
    partner_gender=models.CharField(max_length=20, null=True)
    religion=models.CharField(max_length=20, null=True)
    partner_religion=models.CharField(max_length=20, null=True)
    mothertongue=models.CharField(max_length=20, null=True)
    partner_mothertongue=models.CharField(max_length=20, null=True)
    relationshiptype=models.CharField(max_length=20, null=True)
    edu=models.CharField(max_length=20, null=True)
    partner_edu=models.CharField(max_length=20, null=True)
    profession=models.CharField(max_length=20, null=True)
    partner_profession=models.CharField(max_length=20, null=True)
    datechar=models.CharField(max_length=20, null=True)
    animal=models.CharField(max_length=20, null=True)
    daynight=models.CharField(max_length=20, null=True)
    movie=models.CharField(max_length=20, null=True)
    music=models.CharField(max_length=20, null=True)
    book=models.CharField(max_length=20, null=True)
    minmax=models.CharField(max_length=20, null=True)

    MBTI=models.CharField(max_length=20, null=True)
    interests=models.CharField(max_length=200, null=True)


class Matches(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    matched_with = models.ForeignKey(User,related_name='matched_with_%(class)s_related',on_delete=models.CASCADE)
    swiped_right = models.BooleanField(null=True, default=None)
    swiped_left = models.BooleanField(null=True, default=None)
    match_score_western = models.FloatField(null=True, default=None)


class Global_stats(models.Model):
    binary_question_similarity_mean = models.FloatField()
    binary_question_dissimilarity_mean = models.FloatField()
    binary_question_similarity_std = models.FloatField()
    binary_question_dissimilarity_std = models.FloatField()
    movies_number_of_similarity_mean = models.FloatField()
    movies_number_of_similarity_std = models.FloatField()
    books_number_of_similarity_mean = models.FloatField()
    books_number_of_similarity_std = models.FloatField()
    music_number_of_similarity_mean = models.FloatField()
    music_number_of_similarity_std = models.FloatField()

class Message(models.Model):
    from_user = models.ForeignKey(User,on_delete=models.CASCADE)
    to_user = models.ForeignKey(User,related_name='to_user_%(class)s_related',on_delete=models.CASCADE)
    time_messaged = models.DateTimeField(default=timezone.now)
    content = models.TextField()