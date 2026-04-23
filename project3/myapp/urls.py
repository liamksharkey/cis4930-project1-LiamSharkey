from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('games/', views.games_home, name='games_home'),
    path('games/<int:pk>/', views.games_detail, name='games_detail'),
    path('games/<int:pk>/edit/', views.games_edit, name='games_update'),
    path('games/<int:pk>/delete/', views.games_delete, name='games_delete'),
    path('games/analytics', views.games_analytics, name='games_analytics'),
    path('fetch/', views.fetch_data, name='fetch_data'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)