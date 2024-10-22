from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.user_view, name='user_view'),
    path('create/', create_user, name='create_user'),
    path('<int:pk>/update/', user_update, name='update_user'),
    path('<int:pk>/delete/', user_delete, name='delete_user'),
]
