# Generated by Django 4.2.5 on 2023-09-16 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0002_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='descricao',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
