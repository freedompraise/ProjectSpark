from .manager import UserManager

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db import models
from django.utils.text import slugify


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

    def is_staff(self):
        return False

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True

    def get_full_name(self):
        return self.username

    def get_by_natural_key(self, email):
        return self.get(email=email)

    def get_short_name(self):
        return self.username
    
    def set_password(self, password):
        self.password = password

    def check_password(self, password):
        return self.password == password
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
    tags = models.ManyToManyField('Tag', related_name='ideas', blank=True)
    total_rating = models.IntegerField(default=0, blank=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True)

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

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    def __str__(self):
        return self.name

    @staticmethod
    def generate_unique_slug(tag_name):
        slug = slugify(tag_name)
        unique_slug = slug
        num = 1
        while Tag.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{num}'
            num += 1
        return unique_slug


class IdeaRating(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    rater = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()

    def update_total_rating(self):
        upvotes = self.idea.idearating_set.filter(rating=1).count()
        downvotes = self.idea.idearating_set.filter(rating=-1).count()
        self.idea.total_rating = upvotes - downvotes
        self.idea.save()
        
    class Meta:
        unique_together = ('idea', 'rater')
