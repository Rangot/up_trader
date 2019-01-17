# Generated by Django 2.1.1 on 2019-01-16 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название меню')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Пункт меню')),
                ('text', models.TextField(verbose_name='Описание')),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='options',
            field=models.ManyToManyField(blank=True, related_name='option', to='menu.Option', verbose_name='Пункт меню'),
        ),
    ]