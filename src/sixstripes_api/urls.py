from data import api
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"politicians", api.PoliticianViewSet)
router.register(r"musicians", api.MusicianViewSet)
router.register(r"movies", api.MovieViewSet)
router.register(r"digital-influencers", api.DigitalInfluencerViewSet)
router.register(r"athlets", api.AthletViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("v1/", include(router.urls)),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
