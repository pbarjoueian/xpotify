# Generated by Django 4.2.1 on 2023-06-11 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='history',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]
