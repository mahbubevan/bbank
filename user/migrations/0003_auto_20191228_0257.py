# Generated by Django 3.0.1 on 2019-12-28 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20191228_0254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
