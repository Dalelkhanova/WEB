# Generated by Django 3.0.4 on 2020-03-29 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200329_2351'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='category_id',
        ),
    ]
