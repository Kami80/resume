from django.db import models

# Create your models here.

class TopPage(models.Model):

    firstname = models.CharField(max_length=200, null=True, blank=True)
    lastname = models.CharField(max_length=200, null=True, blank=True)
    short_description = models.TextField(null=True, blank=True)
    featured_image_top = models.ImageField(null=True, blank= True)
    featured_image_bio = models.ImageField(null=True, blank= True)
    work_field = models.CharField(max_length=2000, null=True, blank=True)
    youtube_intro_video_embed = models.CharField(max_length=2000, null=True, blank=True)
    cv_pdf_file = models.FileField(upload_to="static/files/", null=True, blank=True)
    long_description = models.TextField(null=True, blank=True)
    degree = models.CharField(max_length=2000, null=True, blank=True)
    phone = models.CharField(max_length=2000, null=True, blank=True)
    address = models.CharField(max_length=2000, null=True, blank=True)
    birtday = models.CharField(max_length=2000, null=True, blank=True)
    experience = models.CharField(max_length=2000, null=True, blank=True)
    email = models.CharField(max_length=2000, null=True, blank=True)
    freelance = models.CharField(choices=[('unavailable', 'unavailable'), ('available', 'available')], max_length=2000, null=True, blank=True)



    def __str__(self):
        return self.firstname

class Experience(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    company = models.CharField(max_length=200, null=True, blank=True)
    years = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.title


class Education(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    university = models.CharField(max_length=200, null=True, blank=True)
    years = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.title

class Skills(models.Model):
    skill = models.CharField(max_length=200, null=True, blank=True)
    percentage_of_mastery = models.IntegerField(default=0, null=True, blank=True)
    color = [('danger', 'red'), ('primary', 'light blue'), ('success', 'green'),
     ('info', 'blue'), ('warning', 'yellow'), ('dark', 'black'), ('light', 'white')]
    color = models.CharField(choices= color, max_length=2000, null=True, blank=True)
    def __str__(self):
        return self.skill



class Services(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    fa_fa_white_icon = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    link = models.CharField(max_length=500, null=True, blank=True)
    def __str__(self):
        return self.title

class Tags(models.Model):
    tag = models.CharField(max_length=200)
    def __str__(self):
        return self.tag

class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    tag = models.CharField(max_length=200)
    featured_image = models.ImageField(null=True, blank= True)
    def __str__(self):
        return self.title


class Reviews(models.Model):
    name = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank= True)
    def __str__(self):
        return self.name

class Blogs(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    link = models.CharField(max_length=2000, null=True, blank=True)
    date_day = models.CharField(max_length=200, null=True, blank=True)
    date_month = models.CharField(max_length=200, null=True, blank=True)
    date_year = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank= True)
    def __str__(self):
        return self.title
