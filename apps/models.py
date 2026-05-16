from django.db.models import CharField, BooleanField, DateTimeField, Model, IntegerField, ForeignKey, CASCADE


# Create your models here.


class User(Model):
    username = CharField(max_length=255, unique=True)
    email = CharField(max_length=255, unique=True)
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    password = CharField(max_length=50)
    is_active = BooleanField(default=False)
    created_at = DateTimeField(auto_now_add=True)

class Post(Model):
    title = CharField(max_length=255)
    content = CharField(max_length=255)
    is_published = BooleanField(default=False)
    views = IntegerField()
    author_id = ForeignKey(User, on_delete = CASCADE, related_name='author_post')
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

class Comment(Model):
    content = CharField(max_length=255)
    author_id = ForeignKey(User, on_delete = CASCADE, related_name='author_comment')
    post_id = ForeignKey(Post, on_delete = CASCADE, related_name='post')
    created_at = DateTimeField(auto_now_add=True)


