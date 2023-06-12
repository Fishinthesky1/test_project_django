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


class Task(models.Model):
    title = models.CharField("Title", max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(default=one_week_hence)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="images/%Y/%m/%d", null=True, blank=True)
    users = models.ManyToManyField(User, related_name='assigned_tasks')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='authored_tasks', default=get_user_model().objects.first().pk
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='1')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return (self.title)


class Comment(models.Model):
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    task = models.ForeignKey(Task, verbose_name="Задача", on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.task}"
