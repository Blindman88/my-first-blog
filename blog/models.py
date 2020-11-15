from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):       #эта строка определяет нашу модель (объект)
    '''
    class — это специальное ключевое слово для определения объектов.
    Post — это имя нашей модели, мы можем поменять его при желании (специальные знаки и пробелы использовать нельзя). Всегда начинай имена классов с прописной буквы.
    models.Model означает, что объект Post является моделью Django, так Django поймет, что он должен сохранить его в базу данных.
    '''
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #  ссылка на другую модель.Связь многое-к-одному. Принимает позиционный аргумент: класс связанной модели.
    title = models.CharField(max_length=200)    #определяем текстовое поле с ограничением на количество символов.
    text = models.TextField()       #определяется поле для неограниченно длинного текста. Выглядит подходящим для содержимого поста
    created_date = models.DateTimeField(default=timezone.now)   #дата и время.
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):      # Это как раз метод публикации для записи
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title