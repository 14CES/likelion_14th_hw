from django.urls import path
from . import views
from .views import*

app_name='main'
urlpatterns=[
    path('', mainpage, name='mainpage'),
    path('new_post', new_post, name='new_post'),
    path('create', create, name='create'),
    path('post', postpage, name='postpage'),
    path('detail/<int:post_id>', detail, name='detail'),
    path('edit/<int:post_id>', edit, name='edit'),
    path('update/<int:post_id>', update, name='update'),
    path('delete/<int:post_id>', delete, name='delete'),
]