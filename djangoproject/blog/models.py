from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    short_description = models.TextField("Краткое описание", max_length=200)
    text = models.TextField("Текст")
    date = models.DateTimeField("Дата публикации")
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"