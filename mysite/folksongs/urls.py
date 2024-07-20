from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
import django.contrib.auth.urls
from django.http import Http404

# Code was adapted and inspired by the lectures from Dr Scharlau at the University of Aberdeen - in the 'Enterprise Software Development' module.


urlpatterns = [
	path('', views.home, name="home"),
	path('accounts/', include('django.contrib.auth.urls')),
	path('signup/', views.signup, name='signup'),
  path('song/<int:id>/', views.song, name="song"),
  path('song_add/', views.song_add, name= 'song_add'),
  path('search', views.search, name= 'search'),
  path('map', views.map, name= 'map'),
  path('help', views.help, name= 'help'),
	path('404', views.handler404, name="404"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

#handler404 = 'team.views.handler404'