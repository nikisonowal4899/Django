from django.contrib import admin
from django.conf.urls import url, include
from . import views
#Include is a package that lets us include other files

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^music/', include('music.urls')),
    url(r'', views.home_view, name='home_view'),
]
