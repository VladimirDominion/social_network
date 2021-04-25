from django.db import models

from core.models import CreatedUpdatedModel


class PostQueryset(models.QuerySet):
    def with_likes(self):
        return self.annotate(
            count_likes=models.Count('likes', filter=models.Q(likes__kind=True))
        ).annotate(count_dislikes=models.Count('likes', filter=models.Q(likes__kind=False)))


class Post(CreatedUpdatedModel):
    title = models.CharField(max_length=255, default="", db_index=True)
    text = models.TextField(default="")

    author = models.ForeignKey("users.User", on_delete=models.CASCADE)

    objects = models.Manager.from_queryset(PostQueryset)()

    def __str__(self):
        return self.title


class Like(CreatedUpdatedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    kind = models.BooleanField(default=None, null=True, help_text="True = Like | False = Dislike")
