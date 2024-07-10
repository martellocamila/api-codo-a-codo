from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('alta-habitacion/', views.alta_habitacion, name='alta_habitacion'),
    path('store/', views.store, name='store'),
    path('delete/<int:habitacion_id>/', views.delete, name='delete')
]

