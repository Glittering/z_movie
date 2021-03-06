# Generated by Django 3.1.2 on 2020-10-29 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=20, verbose_name='label')),
            ],
            options={
                'verbose_name': 'labels',
                'verbose_name_plural': 'labels',
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='movie name')),
                ('validity', models.CharField(max_length=255, verbose_name='movie validity')),
                ('content', models.CharField(max_length=255, verbose_name='author point')),
                ('douban', models.URLField(verbose_name='douban comment')),
                ('up_time', models.DateTimeField(auto_now_add=True, verbose_name='update time')),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='z_web.movielabel', verbose_name='movie label')),
            ],
            options={
                'verbose_name': 'movies',
                'verbose_name_plural': 'movies',
                'ordering': ('pk',),
            },
        ),
    ]
