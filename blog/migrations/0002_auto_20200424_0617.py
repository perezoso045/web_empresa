# Generated by Django 3.0.5 on 2020-04-24 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-created'], 'verbose_name': 'categoria', 'verbose_name_plural': 'categorias'},
        ),
    ]
