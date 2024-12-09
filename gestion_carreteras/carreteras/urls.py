from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('carreteras/', views.lista_carreteras, name='carreteras'),
    path('carretera/<int:pk>/', views.detalle_carretera, name='carretera_detail'),
    path('carretera/create/', views.crear_carretera, name='carretera_create'),
    path('carretera/<int:pk>/update/', views.editar_carretera, name='carretera_update'),
    path('carretera/<int:pk>/delete/', views.eliminar_carretera, name='carretera_delete'),
    
    # Rutas para los tramos
    path('carretera/<int:carretera_id>/tramos/', views.lista_tramos, name='lista_tramos'),
    path('carretera/<int:carretera_id>/tramo/create/', views.crear_tramo, name='crear_tramo'),
    path('tramo/<int:tramo_id>/edit/', views.editar_tramo, name='editar_tramo'),
    path('tramo/<int:tramo_id>/delete/', views.eliminar_tramo, name='eliminar_tramo'),
    path('tramo/<int:tramo_id>/', views.detalle_tramo, name='detalle_tramo'),
]

