
from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class CourseLog(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='logs')
    action = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.course.title} - {self.action} at {self.timestamp}"
