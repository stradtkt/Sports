# Generated by Django 2.1.3 on 2018-12-17 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drego', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='plans',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Plans',
        ),
    ]
