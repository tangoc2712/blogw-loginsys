# Generated by Django 3.0.3 on 2022-07-18 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_user_status_contribute'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fullname',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
