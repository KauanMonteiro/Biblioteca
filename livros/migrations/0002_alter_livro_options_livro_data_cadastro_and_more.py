# Generated by Django 5.0.1 on 2024-02-19 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='livro',
            options={'verbose_name': 'Livro'},
        ),
        migrations.AddField(
            model_name='livro',
            name='data_cadastro',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='livro',
            name='data_devolucao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='livro',
            name='data_emprestimo',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='livro',
            name='tempo_duracao',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='livro',
            name='autor',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='livro',
            name='descricao',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='livro',
            name='emprestado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='livro',
            name='paginas',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
