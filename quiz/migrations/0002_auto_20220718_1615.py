# Generated by Django 3.2.7 on 2022-07-18 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='option2',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='questions',
            name='option3',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='questions',
            name='option4',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='option1',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
