# Generated by Django 3.2.7 on 2022-07-19 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='answer',
            field=models.CharField(max_length=30, null=True),
        ),
    ]