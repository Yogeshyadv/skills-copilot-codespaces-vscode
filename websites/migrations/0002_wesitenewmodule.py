# Generated by Django 5.1 on 2024-10-08 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WesiteNewModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctors_name', models.CharField(max_length=100)),
                ('doctors_desc', models.CharField(max_length=200)),
                ('doctors_image', models.FileField(default=None, max_length=250, null=True, upload_to='WesiteNewModule')),
            ],
        ),
    ]