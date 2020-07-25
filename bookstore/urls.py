from django.conf.urls import url

from bookstore.views import BookView

urlpatterns = [
    url(r'^index/$', BookView.as_view())
]
