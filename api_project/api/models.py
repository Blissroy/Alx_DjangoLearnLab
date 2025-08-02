from django.db import models

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=13, unique=True)
    page_count = models.IntegerField(null=True, blank=True)
    cover_url = models.URLField(null=True, blank=True)
    language = models.CharField(max_length=20, default='English')

    def _str_(self):
        return f"{self.title} by {self.author}"
