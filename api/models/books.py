from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=255, unique=True)
    author = models.ForeignKey('Authors', on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.title
