from django.db import models


class License(models.Model):
    name = models.CharField(max_length=80, unique=True)
    symbols = models.CharField(max_length=5)
    url = models.URLField(unique=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return self.url

class Licensed(models.Model):
    license = models.ForeignKey(License, on_delete=models.CASCADE)
    class Meta:
        abstract = True


