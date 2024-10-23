from django.urls import path, include
from . import views
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('<int:pk>/', views.research_project_detail, name='project_detail'),
    path('<int:pk>/upload/', views.upload_data, name='upload_data'),
    path('users/', include('users.urls')),  # Ensure users app URLs are included
    path('accounts/', include('django.contrib.auth.urls')),  # Include authentication URLs
]
