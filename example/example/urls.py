from django.conf.urls import include, url

urlpatterns = [
    # ...
    url(r'^examples/', include('emailpal.urls')),
    # ...
]
