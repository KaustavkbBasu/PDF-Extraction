from django.db import models
# from django.utils import timezone
# Create your models here.
class Pdf(models.Model):

    title = models.CharField(max_length=200, null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    keywords = models.CharField(max_length=2000, null=True, blank=True)
    # created = models.DateTimeField(auto_now_add=True)
    # modified = models.DateTimeField(auto_now=True)
    Creator = models.CharField(max_length=200, null=True, blank=True)
    Producer = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField(null=True, blank=True) 
    def __str__(self):
        return self.author
