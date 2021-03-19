# Generated by Django 2.2.6 on 2019-12-07 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0003_album_band'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(to='exercises.Category'),
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('duration', models.DateTimeField(null=True)),
                ('album', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exercises.Album')),
            ],
        ),
    ]