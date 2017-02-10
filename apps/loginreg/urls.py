from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register$', views.register, name="register"),
    url(r'^login$', views.login, name="login"),
    url(r'^test/auth=(?P<uuid>[^/]+)/$', views.test, name="test"),
    #
    # [0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}
]
