# Generated by Django 5.1.2 on 2024-11-02 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('streaming', models.CharField(choices=[('AK', 'Amazon Kindle'), ('FI', 'Físico')], max_length=2)),
                ('nota', models.IntegerField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('categories', models.ManyToManyField(to='livros.categories')),
            ],
        ),
    ]
