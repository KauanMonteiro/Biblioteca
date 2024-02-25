# Generated by Django 5.0.1 on 2024-02-25 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0006_livro_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livro',
            name='category',
        ),
        migrations.AddField(
            model_name='livro',
            name='category',
            field=models.ManyToManyField(to='livros.category'),
        ),
    ]
