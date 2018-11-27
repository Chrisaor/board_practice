from django.db import models

from user.models import User


class DateLog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class Board(DateLog):
    title = models.CharField(max_length=100)
    is_anonymous = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Post(DateLog):
    title = models.CharField(max_length=100)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    is_blind = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comment(DateLog):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='parent')
    comment = models.TextField()
    is_blind = models.BooleanField(default=False)

    def __str__(self):
        return self.comment
