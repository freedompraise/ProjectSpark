from django.db import models
from .manager import UserManager

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.db import models


class User(AbstractBaseUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    objects = UserManager()

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def get_full_name(self):
        return self.username

    def get_by_natural_key(self, email):
        return self.get(email=email)

    def get_short_name(self):
        return self.username

    class Meta:
        app_label = 'api'



    def __str__(self):
        return self.username



class Idea(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment on '{self.idea.title}' by {self.commenter.username}"
