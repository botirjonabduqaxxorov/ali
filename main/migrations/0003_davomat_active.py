# Generated by Django 5.1 on 2024-08-09 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_xodimlar_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='davomat',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
