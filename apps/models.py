from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models import Model, IntegerField, CharField, DateField, TimeField, TextField, BooleanField, ForeignKey, \
    CASCADE, EmailField, DateTimeField, SmallIntegerField, DecimalField


# Create your models here.

class CustomUserManager(UserManager):

    def _create_user_object(self,  email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        return user

    def _create_user(self,email, password, **extra_fields):
        """
        Create and save a user with the given  email, and password.
        """
        user = self._create_user_object( email, password, **extra_fields)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    first_name = CharField(max_length=255,null=True,blank=True)
    objects = CustomUserManager()
    email = EmailField(unique=True)
    last_name = CharField(max_length=255,null=True,blank=True)
    is_active = BooleanField(default=True)
    created_at = DateTimeField(auto_now_add=True)


class Post(Model):
    title = CharField(max_length=255)
    content = CharField(max_length=255)
    is_published = BooleanField(default=False)
    views = IntegerField()
    author_id = ForeignKey(User, on_delete = CASCADE)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

class Comment(Model):
    content = CharField(max_length=255)
    author_id = ForeignKey(User, on_delete = CASCADE)
    post_id = ForeignKey(Post, on_delete = CASCADE)
    created_at = DateTimeField(auto_now_add=True)


