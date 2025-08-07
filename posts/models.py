from django.contrib.auth.models import User
from django.db import models

from app.models import TimeStampMixin

from tags.models import Tag


class Post(TimeStampMixin):
    """
    Моделька Постов наследуется от базового класса TimeStampMixin

    Attributes:
        title (models.CharField): Название Поста
        slug (models.SlugField): Слаг нашего
        description (models.CharField): Описание Нашего Поста
        status (models.CharField): Статус Нашего Поста
        created_at (models.DateTimeField): Дата Создания Поста
        updated_at (models.DateTimeField): Дата Обновление Поста
        published_at (models.DateTimeField): Дата Публикации Поста
        user (User): Пользователь создавший Пост
    """
    STATUS = {
        "df": "Draft",
        "pb": "Publish"
    }

    title = models.CharField(max_length=255, verbose_name="Название Поста")
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=2, choices=STATUS)
    published_at = models.DateTimeField(null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    likes = models.ManyToManyField(User, through="Like", related_name="post_likes")


class PostImage(models.Model):
    """

    """
    image = models.ImageField(upload_to="posts/")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images")


class PostComment(TimeStampMixin):
    """

    """


class Like(TimeStampMixin):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("post", "user")
