from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    MEMBER_TYPE = (
        ('regular', '정회원'),
        ('associate', '준회원'),
        ('admin', '관리자'),
    )
    member_type = models.CharField(max_length=10, choices=MEMBER_TYPE)

    def __str__(self):
        return self.username
