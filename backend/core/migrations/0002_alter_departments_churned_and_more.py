# Generated by Django 4.2.9 on 2024-01-30 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="departments",
            name="churned",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="departments",
            name="functions",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="departments",
            name="new",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="departments",
            name="retained",
            field=models.CharField(max_length=200, null=True),
        ),
    ]