from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('carreteras.urls')),  # Asegúrate de que este `include` esté presente
]
