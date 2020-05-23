from django.contrib import admin
from .models import TodoModel

# Register your models here.

# Modelデータの操作を管理
admin.site.register(TodoModel)
