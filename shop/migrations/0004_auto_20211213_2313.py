# Generated by Django 2.2 on 2021-12-13 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20211207_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='product'),
        ),
    ]
