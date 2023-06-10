from django.db import models

# Create your models here.
class NationalID(models.Model):
    name = models.CharField(max_length=10 , default=' ')
    national_id = models.CharField(max_length=10, unique=True)
    file = models.FileField(upload_to="files/")

    def __str__(self):
        return self.name