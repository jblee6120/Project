from django.db import models
# Create your models here.

class LoadBook(models.Model):

    class Meta:
        db_table = 'Book'

    def __str__(self):
        return self.title

    title = models.CharField(max_length=256, null=True, default=None)
    barcode = models.CharField(max_length=64, null=True, default=None)
    location = models.CharField(max_length=20, null=True, default=None)