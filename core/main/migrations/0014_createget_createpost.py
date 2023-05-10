# Generated by Django 4.2.1 on 2023-05-07 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_title_colored_title4_title_colored_title5_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateGet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Create GET title')),
                ('description', models.CharField(max_length=80, verbose_name='Create GET Description')),
                ('username', models.CharField(max_length=50, verbose_name='Create GET Username')),
                ('price', models.CharField(max_length=100, verbose_name='Create GET Price')),
                ('royalty', models.CharField(max_length=50, verbose_name='Create GET Royalty')),
                ('file_name', models.CharField(max_length=40, verbose_name='Create GET File Name')),
                ('btn_name', models.CharField(max_length=50, verbose_name='Create GET Button Name')),
            ],
            options={
                'verbose_name': 'Create GET',
                'verbose_name_plural': 'Create GET',
            },
        ),
        migrations.CreateModel(
            name='CreatePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_title', models.CharField(max_length=50, verbose_name='User Title')),
                ('user_description', models.CharField(max_length=80, verbose_name='User Description')),
                ('user_name', models.CharField(max_length=50, verbose_name='UserName')),
                ('user_price', models.CharField(max_length=20, verbose_name='User Price')),
                ('user_royalty', models.CharField(max_length=50, verbose_name='User Royalty')),
            ],
            options={
                'verbose_name': 'Create POST',
                'verbose_name_plural': 'Create POST',
            },
        ),
    ]