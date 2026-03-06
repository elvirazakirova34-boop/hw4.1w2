from django.db import models

# Create your models here.

from django.db import migrations, models

class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    age = models.IntegerField(verbose_name="Возраст")
    city = models.CharField(max_length=100, verbose_name="Город")
    email = models.EmailField(verbose_name="Email")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

    def __str__(self):
        return self.name
