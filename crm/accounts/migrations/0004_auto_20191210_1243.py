# Generated by Django 3.0 on 2019-12-10 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_order_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('CAT1', 'Windows'), ('CAT2', 'Doors'), ('CAT3', 'Walls')], max_length=20, null=True),
        ),
    ]