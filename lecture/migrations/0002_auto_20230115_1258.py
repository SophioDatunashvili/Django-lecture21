# Generated by Django 2.2.12 on 2023-01-15 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturer',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subject',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
