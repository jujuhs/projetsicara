# Generated by Django 3.0.7 on 2020-06-29 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0003_nom'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Nom',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='categorie',
        ),
        migrations.AddField(
            model_name='photo',
            name='name',
            field=models.CharField(default='sans nom', max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Label',
        ),
    ]
