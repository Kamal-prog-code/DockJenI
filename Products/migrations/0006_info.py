# Generated by Django 3.1.3 on 2020-11-17 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0005_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemid', models.IntegerField()),
            ],
        ),
    ]