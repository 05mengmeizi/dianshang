from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone = models.CharField(max_length=11, unique=True, null=True, blank=True)
    # 其他字段...

    class Meta:
        db_table = 'users_user' 