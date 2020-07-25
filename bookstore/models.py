from django.db import models

# Create your models here.


class BookInformation(models.Model):
    # 创建字段和字段类型
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
