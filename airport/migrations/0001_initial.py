# Generated by Django 4.2.1 on 2023-05-10 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('passport', models.IntegerField(blank=True, null=True)),
                ('ticket', models.IntegerField(blank=True, null=True)),
                ('dem_register', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]