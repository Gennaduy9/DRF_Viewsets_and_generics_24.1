from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Courses(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    preview_image = models.ImageField(upload_to='course_images/', **NULLABLE, verbose_name='картинка')
    description = models.TextField(**NULLABLE, verbose_name='описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
