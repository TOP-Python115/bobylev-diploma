# Generated by Django 4.1.3 on 2022-11-12 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='picture_id',
            field=models.CharField(default='NULL', max_length=100, null=True),
        ),
    ]
