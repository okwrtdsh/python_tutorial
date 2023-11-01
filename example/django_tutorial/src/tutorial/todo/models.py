from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from tutorial.models import ModelBase


class Category(ModelBase):
    """カテゴリー"""

    class Meta:
        verbose_name = verbose_name_plural = "カテゴリー"
        ordering = ["order"]

    name = models.CharField("名称", max_length=255)
    order = models.PositiveIntegerField("表示順")

    def __str__(self):
        return self.name


class ToDoUser(User):
    """ユーザー"""

    class Meta:
        verbose_name = verbose_name_plural = "ToDoUser"
        ordering = ["-date_joined"]

    handle_name = models.CharField("表示名", max_length=255)

    def __str__(self):
        return self.handle_name


class ToDo(ModelBase):
    """ToDo"""

    class Meta:
        verbose_name = verbose_name_plural = "ToDo"

    user = models.ForeignKey(
        ToDoUser, verbose_name="ユーザー", on_delete=models.PROTECT)
    categories = models.ManyToManyField(Category, verbose_name="カテゴリー")

    name = models.CharField("名称", max_length=255)
    deadline = models.DateTimeField("締め切り")
    completed = models.DateTimeField("完了日時", null=True, blank=True)

    PRIORITY_HIGH = 1
    PRIORITY_MIDDLE = 2
    PRIORITY_LOW = 3
    PRIORITY_CHOICES = (
        (PRIORITY_HIGH, "高"),
        (PRIORITY_MIDDLE, "中"),
        (PRIORITY_LOW, "低"),
    )
    priority = models.PositiveIntegerField("優先度", choices=PRIORITY_CHOICES)
    note = models.TextField("備考", blank=True)

    def __str__(self):
        return self.name

    @property
    def is_completed(self):
        return self.completed is not None

    def complete(self):
        self.completed = timezone.now()
        self.save()
