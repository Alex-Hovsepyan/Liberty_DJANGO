# Generated by Django 4.2.1 on 2023-05-09 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_homeitemscontent_bit_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeitemscontent',
            name='img3',
            field=models.ImageField(default=1, upload_to='images', verbose_name='Image 3'),
            preserve_default=False,
        ),
    ]
