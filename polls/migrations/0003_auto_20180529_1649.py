# Generated by Django 2.0.5 on 2018-05-29 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20180529_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reward',
            name='artefacts',
            field=models.CharField(default='Nothing', max_length=255),
        ),
    ]
