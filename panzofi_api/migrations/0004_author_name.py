# Generated by Django 5.1.2 on 2024-11-04 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panzofi_api', '0003_alter_author_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='name',
            field=models.TextField(null=True),
        ),
    ]