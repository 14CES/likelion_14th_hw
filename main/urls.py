from django.urls import path
from . import views
from .views import*

app_name='main'
urlpatterns=[
    path('', mainpage, name='mainpage'),
    path('second/', secondpage, name='secondpage'),
    path('new_post', new_post, name='new_post'),
    path('create', create, name='create'),
    path('post', postpage, name='postpage'),
    path('detail/<int:post_id>', detail, name='detail'),
    path('edit/<int:post_id>', edit, name='edit'),
    path('update/<int:post_id>', update, name='update'),
    path('delete/<int:post_id>', delete, name='delete'),
    path('edit_comment/<int:comment_id>', edit_comment, name='edit_comment'),
    path('update_comment/<int:comment_id>', update_comment, name='update_comment'),
    path('delete_comment/<int:comment_id>', delete_comment, name='delete_comment'),
]