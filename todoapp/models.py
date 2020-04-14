from django.db import models

# Create your models here.


class TodoItems(models.Model):
    id = models.IntegerField(primary_key=True)
    item = models.CharField(max_length=100)

    def __str__(self):
        return self.item
