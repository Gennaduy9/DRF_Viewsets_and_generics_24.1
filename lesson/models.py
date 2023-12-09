from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Lessons(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(**NULLABLE, verbose_name='описание')
    preview_image = models.ImageField(upload_to='course_images/', **NULLABLE, verbose_name='картинка')
    video = models.TextField(**NULLABLE, verbose_name='ссылка на видео')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
