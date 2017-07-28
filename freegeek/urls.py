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
import django.contrib.auth.views
from diary import urls as diary_urls
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from . import views


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    url(r'^$', views.home),
    url(r'^api/?', include(router.urls)),
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
    ]
