# Generated by Django 3.0.2 on 2020-03-15 10:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0006_auto_20200315_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='acheivements',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='professor',
            name='contact_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='professor',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='professor',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='professor',
            name='stream',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='professor',
            name='url',
            field=models.URLField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='student',
            name='acheivements',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='contact_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='stream',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='url',
            field=models.URLField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='student',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]