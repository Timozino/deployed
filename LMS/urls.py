from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib import admin
from django.urls import path, include
from user import views
#from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

#from django.contrib.auth import views as auth_views
from .ads import AdsView


urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('', include('app.urls')),
    path('accounts/', include('user.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login', views.login, name='login'),
    #path('ads.txt', TemplateView.as_view(template_name='ads.txt', content_type='text/plain')),
    
    # path('login/', views.user_login, name='login'),
    path(
        "ads.txt",
        RedirectView.as_view(url=staticfiles_storage.url("ads.txt")),
    ),
    
    path('ads.txt', AdsView.as_view()),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)