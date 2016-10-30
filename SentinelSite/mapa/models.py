from django.db import models
from django.utils import timezone


class Warstwa(models.Model):
    plik = models.FileField(upload_to='~', max_length=200)
    czyWektor = models.BooleanField()
    #author = models.ForeignKey('auth.User')
    epsg = models.CharField(max_length=200)
    comment = models.TextField()
    data = models.DateTimeField(
            default=timezone.now)
    def typ(self):
        # ternary-conditional-operator
        return 'wektor' if self.czyWektor else 'raster'
    def pokaz(self):
        pass
    def __str__(self):
        return self.comment
