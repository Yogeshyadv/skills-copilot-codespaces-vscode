# Generated by Django 5.1 on 2024-10-01 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebsiteModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icons_entry', models.CharField(max_length=200)),
                ('title_entry', models.CharField(max_length=250)),
                ('desc_content', models.TextField()),
            ],
        ),
    ]