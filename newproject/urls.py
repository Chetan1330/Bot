from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('newadmin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

    path('', include('authentication.urls')),



    path('', include('DasboardApp.urls')),

]