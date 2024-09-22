from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

from django.db import models

class RotateArray(models.Model):
    nums = models.CharField(max_length=255)
    k = models.IntegerField()

class KthLargestElement(models.Model):
    nums = models.CharField(max_length=255)
    k = models.IntegerField()

class LongestIncreasingPath(models.Model):
    matrix = models.TextField()

