# Generated by Django 2.2.5 on 2019-10-07 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyFirst', '0006_auto_20191007_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empdata',
            name='empID',
            field=models.IntegerField(editable=False, primary_key=True, serialize=False),
        ),
    ]
