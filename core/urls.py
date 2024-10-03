from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/defender/', include('defender.urls')), # defender admin
    path('admin/', admin.site.urls),

    path('', include('crm.urls')),
    path('management/', include('management.urls')),


]
