# Generated by Django 4.1.5 on 2023-01-24 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='제목')),
                ('content', models.TextField(verbose_name='내용')),
                ('like', models.BooleanField(default=False, verbose_name='좋아요')),
            ],
        ),
    ]
