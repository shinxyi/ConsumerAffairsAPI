from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('apps.loginreg.urls', namespace="users")),
    url(r'^companies/', include('apps.companies.urls', namespace="companies")),
    url(r'^reviews/', include('apps.reviews.urls', namespace="reviews"))
]
