from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^$', views.index, name='welcome'),
    url(r'^driver/profiles/', views.Driver_Prof, name='driver'),
    url(r'^profiles/edit/', views.edituserprofile, name='edituserprofile'),
    url(r'^profile/', views.user_profile, name='user_profile'),
    # url(r'^driver/profiles/edit/',views.edit_driver,name='editDriverProfile')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
