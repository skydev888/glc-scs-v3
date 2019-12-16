# Generated by Django 2.1.5 on 2019-12-16 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_userprofile_password3'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='password3',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
