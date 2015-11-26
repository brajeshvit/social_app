from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^logged/$','login_app.views.logged'),
    url(r'^logout/$','login_app.views.logout'),
    url(r'^login/$','login_app.views.login'),
    url('', include('social.apps.django_app.urls', namespace='social')),
)
