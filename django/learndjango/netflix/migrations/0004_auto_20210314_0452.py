# Generated by Django 3.1.4 on 2021-03-14 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netflix', '0003_auto_20210314_0431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='src',
            field=models.FileField(upload_to='netflix/movies/videos'),
        ),
    ]
