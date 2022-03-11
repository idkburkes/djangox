from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Task(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(default='')
    create_date_time = models.DateTimeField(auto_now_add=True)
    due_date_time = models.DateTimeField()
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='creator')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task_detail', args=[str(self.id)])


