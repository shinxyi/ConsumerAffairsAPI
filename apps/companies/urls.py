from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create$', views.create, name="create_company"),
    url(r'^index$', views.index, name="index_all_companies"),
    url(r'^(?P<id>\d+)$', views.get_one, name="get_one_company"),
]
