# Generated by Django 4.2.1 on 2023-05-07 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_title_colored_title3_title_title3'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeItemsPath',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path1', models.CharField(max_length=50, verbose_name='Home Items Path 1')),
                ('path2', models.CharField(max_length=50, verbose_name='Home Items Path 2')),
                ('path3', models.CharField(max_length=50, verbose_name='Home Items Path 3')),
                ('path4', models.CharField(max_length=50, verbose_name='Home Items Path 4')),
                ('path5', models.CharField(max_length=50, verbose_name='Home Items Path 5')),
            ],
        ),
    ]