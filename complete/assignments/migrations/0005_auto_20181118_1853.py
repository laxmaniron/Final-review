# Generated by Django 2.1.3 on 2018-11-18 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0004_tasklist_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Todolist'),
        ),
    ]
