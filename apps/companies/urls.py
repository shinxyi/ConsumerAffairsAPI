from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create/auth=(?P<uuid>[^/]+)/$', views.create, name="create_company"),
    url(r'^index/auth=(?P<uuid>[^/]+)/$', views.index, name="index_all_companies"),
    url(r'^company=(?P<company_name>[^/]+)/auth=(?P<uuid>[^/]+)/$', views.get_one, name="get_one_company"),
]
