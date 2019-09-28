from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include, url
from core import views

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),

    path('', views.video_list, name='video_list'),#Home
    path('videos/upload', views.upload_video, name='upload_video'),#UploadsVideo

    #path('search', views.search, name='search'),
    #path('filter', views.filter, name='filter'),

    path('video_edit/<int:id>/', views.video_edit, name="video_edit"),
]  

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
