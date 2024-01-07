# Generated by Django 4.2.5 on 2023-09-15 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=7)),
                ('desc', models.TextField()),
            ],
        ),
    ]