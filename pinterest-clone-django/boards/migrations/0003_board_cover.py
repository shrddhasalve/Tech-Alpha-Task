# Generated by Django 4.0.1 on 2022-01-31 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='cover',
            field=models.ImageField(default='default.png', upload_to='pins'),
        ),
    ]
