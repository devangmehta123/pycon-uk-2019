from django.conf.urls import url
from .dist_ids import DistIdsView

urlpatterns = [
    url(
        r'^partner-resources/(?P<affiliate_id>[a-zA-Z0-9\-_]*)/dist-ids/$',
        DistIdsView.as_view(),
        name='dist_ids'
    ),
]
