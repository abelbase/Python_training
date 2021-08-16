from django.db import models

# Create your models here.
class student_info(models.Model):
    Name = models.CharField(max_length=100)
    IDs = models.IntegerField()
    Contact = models.CharField(max_length=10)

    def __str__(self):
        return self.Name


