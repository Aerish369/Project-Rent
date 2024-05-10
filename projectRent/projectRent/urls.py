from django.contrib import admin
from django.urls import path, include

from users import urls
from rentListings import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('rentListings.urls')),
]
