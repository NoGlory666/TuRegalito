# Generated by Django 2.2.4 on 2019-08-30 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='continents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('names', models.CharField(max_length=50)),
                ('descriptions', models.CharField(max_length=50)),
            ],
        ),
    ]
