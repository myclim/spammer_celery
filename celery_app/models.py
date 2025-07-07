from django.db import models




class EmailUser(models.Model):
    user = models.CharField(max_length=100, unique=True, verbose_name='Пользователь')
    email = models.EmailField(max_length=150, unique=True, verbose_name='email')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.user}: ({self.email})'
