from django.urls import path
from todolist.views import create_new_todolist, delete_task, ganti_status, show_todolist
from todolist.views import register #sesuaikan dengan nama fungsi yang dibuat
from todolist.views import login_user #sesuaikan dengan nama fungsi yang dibuat
from todolist.views import logout_user

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_new_todolist, name='create_new_todolist'),
    path('delete_task/<int:id>/', delete_task, name='delete_task'),
    path('set_status/<int:id>/', ganti_status, name='ganti_status'),
]