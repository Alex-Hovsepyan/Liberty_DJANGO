# Generated by Django 4.2.1 on 2023-05-06 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_homepagecategory_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images', verbose_name='HomePage Collection')),
                ('title', models.CharField(max_length=50, verbose_name='HomePage Collection')),
                ('subtitle1', models.CharField(max_length=50, verbose_name='HomePage SubTitle 1')),
                ('subtitle1_info', models.CharField(max_length=50, verbose_name='HomePage Subtitle 1 Info')),
                ('subtitle2', models.CharField(max_length=50, verbose_name='HomePage SubTitle 2')),
                ('subtitle2_info', models.CharField(max_length=50, verbose_name='HomePage Subtitle 2 Info')),
                ('btn_name', models.CharField(max_length=40, verbose_name='HomePage Collection Button Name')),
            ],
        ),
    ]
