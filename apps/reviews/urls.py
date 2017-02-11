from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^create/company=(?P<company_id>\d+)/auth=(?P<uuid>[^/]+)/$', views.create, name="create_review"),
    url(r'^index/auth=(?P<uuid>[^/]+)/$', views.index, name="index_my_reviews"),
]
