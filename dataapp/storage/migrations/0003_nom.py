# Generated by Django 3.0.7 on 2020-06-26 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0002_auto_20200626_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]