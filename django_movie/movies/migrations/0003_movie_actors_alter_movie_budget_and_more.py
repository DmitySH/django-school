# Generated by Django 4.0 on 2021-12-23 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_rating_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='actor', to='movies.Actor', verbose_name='Актеры'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='budget',
            field=models.PositiveIntegerField(default=0, help_text='сумма в долларах', verbose_name='Бюджет'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='directors',
            field=models.ManyToManyField(related_name='film_director', to='movies.Actor', verbose_name='Режиссеры'),
        ),
    ]
