from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    adds = models.TextField('Дополнительно')

    def __str__(self):
        return self.title
