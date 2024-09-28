from django.db import models
from django.contrib.auth.models import User
from django.db.models import UniqueConstraint


class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey('Books', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['user', 'book'], name='uk_favorites_user_book'),
        ]
        verbose_name_plural = 'Favorites'
        verbose_name = 'Favorite'
