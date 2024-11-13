from django.db import models

# Create your models here.
class WebsiteModule(models.Model):
    icons_entry=models.CharField(max_length=200)
    title_entry=models.CharField(max_length=250)
    desc_content=models.TextField()


class WesiteNewModule(models.Model):
    doctors_name=models.CharField(max_length=100)
    doctors_desc=models.CharField(max_length=200)
    doctors_image=models.FileField(upload_to="WesiteNewModule",max_length=250,null=True,default=None)


class ContactForm(models.Model):
    first_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    GENDER_CHOICES = (
        (1, 'Male'),
        (2, 'Female'),
        (3, 'Others'),
    )
    gender = models.IntegerField(choices=GENDER_CHOICES)

    DEPARTMENT_OPTIONS = (
        (1, 'Physiotherapy'),
        (2, 'Physical Health'),
        (3, 'Treatments'),
    )
    department = models.IntegerField(choices=DEPARTMENT_OPTIONS)

    date = models.DateField()
    comments = models.TextField()

