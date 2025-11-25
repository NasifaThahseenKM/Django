from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    result = models.CharField(max_length=100)   # e.g. "Passed", "Failed", "A Grade"

    def __str__(self):
        return self.name
