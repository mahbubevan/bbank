# Generated by Django 3.0.1 on 2019-12-27 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donate_to', models.IntegerField()),
                ('donate_from', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=150)),
                ('blood_group', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('gender', models.IntegerField(default=0)),
                ('status', models.CharField(max_length=20)),
                ('helping_count', models.IntegerField(default=0)),
                ('donate', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.Donate')),
            ],
        ),
    ]