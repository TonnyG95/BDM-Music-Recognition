from django.contrib import admin
from django.urls import path
from base.views import home, scan_song

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('scan_song/', scan_song, name='scan_song'),
    

]
