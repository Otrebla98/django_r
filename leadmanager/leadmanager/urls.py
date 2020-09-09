from django.contrib import admin
from django.urls import path, include

from django.confing import settings
from django.config.urls.static import static


urlpatterns = [
    path('', include('frontend.urls')),
    path('', include('leads.urls')),
    path('', include('accounts.urls'))
] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
