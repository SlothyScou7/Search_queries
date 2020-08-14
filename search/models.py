from django.db import models

class City(models.Model):
    name = models.CharField(max_length=255,unique=True)
    state = models.CharField(max_length=255,unique=True)

    class Meta:
      verbose_name_plural = "cities"

    def __str__(self):
        return self.name
