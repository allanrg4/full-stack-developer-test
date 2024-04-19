from django.db import models


class Assignment(models.Model):
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE)
    session = models.ForeignKey('meetings.Session', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
