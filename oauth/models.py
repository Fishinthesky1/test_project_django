from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=150, unique=True)
    join_date = models.DateTimeField(auto_now_add=True)
    display_name = models.CharField(max_length=35, blank=True, null=True)
    avatar = models.ImageField(
        upload_to="todo_list/media/avatar",
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg'])]
    )
    def __str__(self):
        return self.email
    @property
    def is_authenticated(self):
        """
        Always return True, check authentication of users
        :return:
        """
        return True
