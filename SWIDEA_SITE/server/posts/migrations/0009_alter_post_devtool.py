# Generated by Django 4.1.5 on 2023-01-18 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_alter_post_devtool'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='devtool',
            field=models.CharField(max_length=50, verbose_name='예상개발툴'),
        ),
    ]