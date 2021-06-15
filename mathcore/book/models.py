from django.db import models

# Create your models here.
class BookList(models.Model):
    name = models.CharField(max_length=15)
    time = models.DateTimeField()
    answer = models.CharField(max_length=30)

    def __str__(self):
        return self.name


