from django.conf.urls import url

from .views import *

urlpatterns = (
    url(r"^login/$", LoginViewSet.as_view()),
    url(r"^clubinfo/$",ClubInfo.as_view()),
    url(r"^clubLowerAdmin/$",clubLowerAdmin.as_view())
)
