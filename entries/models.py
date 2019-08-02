from django.db import models
from model_utils import Choices


# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=100)
    ROSHAN = 'Roshan Pandey'
    BHARAT = 'Bharat Hasija'
    authors = [(ROSHAN, 'Roshan Pandey'),(BHARAT, 'Bharat Hasija')]
    author = models.CharField(max_length=20,choices=authors,default=ROSHAN)
    text= models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Entries'