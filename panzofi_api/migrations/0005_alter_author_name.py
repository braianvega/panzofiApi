# Generated by Django 5.1.2 on 2024-11-04 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panzofi_api', '0004_author_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.TextField(),
        ),
    ]
