
from django.contrib import admin
from django.urls import path, include

# 空白''のときアプリを呼び出す
# adminで管理画面入る
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls'))
]
