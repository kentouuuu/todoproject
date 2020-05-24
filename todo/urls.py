from django.urls import path
from .views import TodoList, TodoDetail,TodoCreate,TodoDelete,TodoUpdate

# classの場合は.as_view()をつける
urlpatterns = [
    path('list/',TodoList.as_view(), name='list'),
    # int型でpkを指定することで、modelオブジェクトにあるpkを付属してくれる
    path('detail/<int:pk>',TodoDetail.as_view(), name='detail'),
    path('create/',TodoCreate.as_view(), name='create'),
    # int型でpkを指定することで、削除/更新データを指定できる
    path('delete/<int:pk>',TodoDelete.as_view(), name='delete'),   
    path('update/<int:pk>',TodoUpdate.as_view(), name='update'),  
    ]