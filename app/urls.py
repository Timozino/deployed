from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

#app_name='App'
urlpatterns = [
    path('base/', views.base, name='base'),
    path('error', views.page_not_found, name = 'error'),
    path('', views.home, name='home'),
    path('single/course/', views.single_course, name= 'single_course'),
    path('course/filter-data',views.filter_data,name="filter-data"),
    path('course/<slug:slug>', views.course_details, name ='course_details'),
    path('search', views.search_course, name="search_course"),
    path('contact', views.contact_us, name='contact_us'),
    path('about', views.about_us, name ='about_us'),
    path('checkout/<slug:slug>', views.checkout, name="checkout"),
   # path('accounts/register', )
    path('my-course', views.my_course, name='my-course'),
    path('course/watch-course/<slug:slug>',views.watch_course, name='watch_course'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
