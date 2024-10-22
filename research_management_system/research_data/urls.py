from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('<int:pk>/', views.research_project_detail, name='project_detail'),
    path('<int:pk>/upload/', views.upload_data, name='upload_data'),
]
