# Generated by Django 5.0.1 on 2024-02-03 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ap', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
