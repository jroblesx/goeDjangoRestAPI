from django.conf.urls import url
from provider import views

urlpatterns = [
    url(r'^providers/', views.ProviderList.as_view()),
    url(r'^provider/(?P<pk>[0-9]+)/$', views.ProviderDetail.as_view()),
    url(r'^serviceareas/', views.ServiceAreasList.as_view()),
    url(r'^servicearea/(?P<pk>[0-9]+)/$', views.ServiceAreasDetail.as_view()),
    url(r'^serviceareafinder/(?P<pos>\-?\d{1,2}\.\d+?\,\-?\d{1,2}\.\d+)$',
        views.FindServiceAreaArround.as_view()),
]
