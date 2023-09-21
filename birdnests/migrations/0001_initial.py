# Generated by Django 4.2.5 on 2023-09-21 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('Library', 'Library'), ('Framework', 'Framework'), ('Video', 'Video'), ('Document', 'Document')], max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]
