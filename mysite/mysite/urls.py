from django.contrib import admin
from home import views
from django.conf.urls import url, include #Include is a package that lets us include other files
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^music/', include('music.urls'), name='music'),
    #url(r'', views.home_view, name='home_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)