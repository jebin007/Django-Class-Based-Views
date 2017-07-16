from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.TeamListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.TeamDeatilView.as_view(), name='detail'),
]
