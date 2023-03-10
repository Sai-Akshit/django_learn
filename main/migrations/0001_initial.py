# Generated by Django 4.1.7 on 2023-03-10 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('isMale', models.BooleanField(default=True)),
                ('age', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
    ]
