# Generated by Django 4.1.3 on 2022-12-15 11:48

from django.db import migrations, models
import videos.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Caption', models.CharField(max_length=100)),
                ('Video', models.FileField(upload_to='media/video/%y', validators=[videos.validators.file_size])),
            ],
        ),
    ]
