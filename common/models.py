from django.db import models

class BookList(models.Model):
    class Meta:
        db_table = "library_booklist"
    
    def __str__(self):
        return self.title
    
    title = models.CharField(max_length=256, null=False)
    author = models.CharField(max_length=64, null=False)
    barcode = models.CharField(max_length=64, null=True)
    book_in_here = models.BooleanField(default=True)
    location = models.CharField(max_length=20)
    section = models.CharField(max_length=256, null=False)