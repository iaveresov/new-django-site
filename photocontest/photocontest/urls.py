from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main_page/', include('main.urls')),
    path('', RedirectView.as_view(url='main_page', permanent=True)),
]
