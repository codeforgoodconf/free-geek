"""freegeek URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers
import django.contrib.auth.views
from diary import urls as diary_urls
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from . import views

router = routers.DefaultRouter()
router.register(r'customers', views.CustomerViewSet, base_name='customers')
router.register(r'resources', views.ResourceViewSet, base_name='resources')
router.register(r'treatments', views.TreatmentViewSet, base_name='treatments')
router.register(r'entries', views.EntryViewSet, base_name='entries')

urlpatterns = [
    url(r'^$', views.home),
    url(r'^api/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^accounts/login/$', django.contrib.auth.views.login),
    url(r'^accounts/logout/$',
        django.contrib.auth.views.logout,
        {'next_page': '/'}),
    url(r'^accounts/password/reset/$',
        django.contrib.auth.views.password_reset,
        {'post_reset_redirect': '/accounts/password/reset/done/'},
        name="password_reset"),
    url(r'^accounts/password/reset/done/$',
        django.contrib.auth.views.password_reset_done),
    url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        django.contrib.auth.views.password_reset_confirm,
        {'post_reset_redirect': '/accounts/password/done/'},
        name='password_reset_confirm'),
    url(r'^accounts/password/done/$',
        django.contrib.auth.views.password_reset_complete),
    url(r'^diary/', include(diary_urls.urlpatterns, namespace='diary')),
    url(r'^diary/?', views.diary, name="diary_home"),
    url(r'^testview/(?P<slug>[\w\-]+)/$', views.LocationDetailView.as_view(), 
        name='locationdetail'),
    url(r'^testview/(?P<locationslug>[\w\-]+)/(?P<slug>[\w\-]+)/$', views.StationDetailView.as_view(), 
        name='stationdetail'),
    url(r'^testview/$', views.IndexView.as_view(), name='index'),
    ]
