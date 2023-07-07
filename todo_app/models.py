from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class TaskStatus(models.IntegerChoices):
    STUCK = 1, 'Stuck'
    WORKING = 2, 'Working'
    DONE = 3, 'Done'


class TimestampedModel(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)


class Task(TimestampedModel):
    title = models.CharField("Title", max_length=100)
    due_date = models.DateTimeField(default=one_week_hence)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="images/%Y/%m/%d", null=True, blank=True)
    users = models.ManyToManyField(User, related_name='assigned_tasks')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='authored_tasks', null=True, default=None
    )
    status = models.IntegerField(choices=TaskStatus.choices, default=TaskStatus.STUCK)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return (self.title)


class Comment(TimestampedModel):
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение")
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    task = models.ForeignKey(Task, verbose_name="Задача", on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"{self.name} - {self.task}"
