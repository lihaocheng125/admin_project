from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):
    ACCOUNT_TYPE_CHOICES = (
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE_CHOICES)
    last_login_time = models.DateTimeField(default=timezone.now)
    login_duration = models.CharField(max_length=50, default='')
    # 添加姓名字段
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='姓名') # 新增用法
    # 添加 related_name 参数
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='custom_user_set'  # 修改反向访问器名称
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_user_set'  # 修改反向访问器名称
    )

class Project(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=200)
    project_file = models.FileField(upload_to='projects/')
    upload_date = models.DateTimeField(default=timezone.now)