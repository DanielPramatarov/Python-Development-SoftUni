# Generated by Django 2.2.5 on 2020-11-25 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20201124_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='UserProfile',
            name='Email',
            field=models.EmailField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='UserProfile',
            name='Phone_number',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='UserProfile',
            name='adress',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='UserProfile',
            name='data_of_birth',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='UserProfile',
            name='facebook_url',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='UserProfile',
            name='firstname',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='UserProfile',
            name='instagram_url',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='UserProfile',
            name='lastname',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='UserProfile',
            name='twitter_url',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
