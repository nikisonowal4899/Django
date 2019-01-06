from django.contrib import admin
from home import views
from django.conf.urls import url, include
#Include is a package that lets us include other files

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^music/', include('music.urls'), name='music'),
    url(r'', views.home_view, name='home_view'),
]
