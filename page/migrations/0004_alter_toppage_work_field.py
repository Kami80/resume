# Generated by Django 4.0.4 on 2022-05-30 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_alter_toppage_freelance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toppage',
            name='work_field',
            field=models.FileField(blank=True, null=True, upload_to='static/files/'),
        ),
    ]
