# Generated by Django 3.0.2 on 2020-03-12 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20200313_0137'),
    ]

    operations = [
        migrations.AddField(
            model_name='join_team',
            name='status',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
