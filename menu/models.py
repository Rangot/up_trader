from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название меню')
    # 2 таблички: узлы и меню. В узлах - ссылка на меню, в каждом узле - ссылка на родителя
    # чтобы сформировать дерево нужно использовать рекурсию


class Option(models.Model):
    menu = models.ForeignKey('Menu', models.DO_NOTHING, blank=True, verbose_name='Название меню')
    title = models.CharField(max_length=100, verbose_name='Пункт меню')


class InnerOption(models.Model):
    option = models.ForeignKey('Option', models.DO_NOTHING, blank=True, verbose_name='Пункт меню')
    title = models.CharField(max_length=100, verbose_name='Вложенный пункт меню')
    text = models.TextField(verbose_name='Описание')
