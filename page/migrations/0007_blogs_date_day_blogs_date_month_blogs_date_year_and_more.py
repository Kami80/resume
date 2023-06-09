# Generated by Django 4.0.4 on 2022-05-30 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0006_skills_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='date_day',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='blogs',
            name='date_month',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='blogs',
            name='date_year',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='link',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
