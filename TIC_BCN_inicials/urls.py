from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('centre/', include('centre.urls')),
    path('authentication/', include('authentication.urls')),
]
