# Generated by Django 5.0.1 on 2024-02-25 13:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0005_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='livros.category'),
        ),
    ]
