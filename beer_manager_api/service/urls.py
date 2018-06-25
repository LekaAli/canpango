from django.conf.urls import url, include
from routers import urlpatterns


urlpatterns = [
	url(r'endpoints/', include(urlpatterns))
]