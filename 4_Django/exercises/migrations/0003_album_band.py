# Generated by Django 2.2.6 on 2019-12-07 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0002_populate'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='band',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exercises.Band'),
        ),
    ]