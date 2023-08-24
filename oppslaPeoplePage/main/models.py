from django.db import models

# Create your models here.
class seminarPPT(models.Model):
    people = models.CharField(max_length=10)
    uploadDate = models.DateField(auto_created=True)
    pptFile = models.FileField()