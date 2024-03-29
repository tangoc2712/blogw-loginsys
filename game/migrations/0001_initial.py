# Generated by Django 3.0.3 on 2022-07-17 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(verbose_name='Level')),
                ('description', models.TextField(verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=255, verbose_name='Word')),
                ('description', models.TextField(verbose_name='Description')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Level')),
            ],
        ),
    ]
