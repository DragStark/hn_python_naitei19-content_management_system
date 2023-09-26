# Generated by Django 4.2.5 on 2023-09-20 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default='download.jpg', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='article',
            name='subtitle',
            field=models.CharField(default='', max_length=200),
        ),
    ]