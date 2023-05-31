from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()

STATUS_CHOICES = (
    ('1', 'Stuck'),
    ('2', 'Working'),
    ('3', 'Done'),
)

def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)

class ListTask(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

class Task(models.Model):
    title = models.CharField("Title", max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(default=one_week_hence)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="images/%Y/%m/%d")
    assign = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks', default=False, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authored_tasks')
    Status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='1')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return (self.title)