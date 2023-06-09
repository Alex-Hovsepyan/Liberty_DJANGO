# Generated by Django 4.2.1 on 2023-05-09 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_generaltitle_page_name5_generaltitle_subtitle5_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='generaltitle',
            name='page_name6',
            field=models.CharField(default=1, max_length=50, verbose_name='General Title Page Name 6'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='generaltitle',
            name='subtitle6',
            field=models.CharField(default=1, max_length=80, verbose_name='General Title Subtitle 6'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='generaltitle',
            name='title6',
            field=models.CharField(default=1, max_length=50, verbose_name='General Title 6'),
            preserve_default=False,
        ),
    ]
