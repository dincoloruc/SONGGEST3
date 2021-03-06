# Generated by Django 3.1.4 on 2021-01-08 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20210108_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='BPM',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='acousticness',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='danceability',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='energy',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='length',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='liveness',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='loudness',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='popularity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='speechiness',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='valance',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='year',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
