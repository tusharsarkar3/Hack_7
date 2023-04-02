# Generated by Django 4.1.7 on 2023-04-01 22:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Matching', '0005_global_stats_questions_mbti_questions_animal_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='matches',
            name='match_score_western',
            field=models.FloatField(default=None, null=True),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_messaged', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', models.TextField()),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user_%(class)s_related', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
