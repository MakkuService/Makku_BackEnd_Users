# Generated by Django 4.1.2 on 2023-02-02 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="auth_user_additional",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("city", models.CharField(blank=True, max_length=40, null=True)),
                ("coordinate", models.CharField(blank=True, max_length=40, null=True)),
                ("IP", models.CharField(blank=True, max_length=20, null=True)),
                ("lastpayment", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "description",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
            ],
        ),
    ]