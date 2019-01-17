from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название меню')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Родитель')

    def __str__(self):
        return self.title

    def get_elder_ids(self):
        if self.parent:
            return self.parent.get_elder_ids() + [self.parent.id]
        else:
            return []

    def children(self):
        return self.menu_set.all()
