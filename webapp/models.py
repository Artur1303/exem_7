from django.core.validators import MinLengthValidator
from django.db import models


class Pol(models.Model):
    question = models.TextField(max_length=2000, verbose_name='Вопрос')
    datetime = models.DateTimeField(auto_now=True, verbose_name='Дата и время')

    def __str__(self):
        return f'{self.question} - {self.datetime}'

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Choice(models.Model):
    Option_text = models.TextField(max_length=2000,verbose_name='Текст Варианта')
    interview = models.ForeignKey('webapp.Pol', related_name='interview',
                                  on_delete=models.CASCADE, verbose_name='Опрос')


class Answer(models.Model):
    poll = models.ForeignKey('webapp.Pol', related_name='answer',
                                        on_delete=models.CASCADE, verbose_name='Ответ')
    creat_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    possible_answer = models.ForeignKey('webapp.Choice', related_name='answer',
                                        on_delete=models.CASCADE, verbose_name='Ответ')