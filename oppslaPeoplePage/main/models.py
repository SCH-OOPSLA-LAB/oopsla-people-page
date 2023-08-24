from django.db import models

# Create your models here.
class SeminarPPT(models.Model):
    id = models.AutoField(primary_key=True)
    people = models.CharField(max_length=10)
    uploadDate = models.DateField(auto_created=True)
    pptFile = models.FileField()