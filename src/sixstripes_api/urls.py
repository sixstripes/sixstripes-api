from data import api
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"politicians", api.PoliticianViewSet)
router.register(r"musicians", api.MusicianViewSet)
router.register(r"movies", api.MovieViewSet)
router.register(r"digital-influencers", api.DigitalInfluencerViewSet)
router.register(r"athlets", api.AthletViewSet)
router.register(r"scientists", api.ScientistViewSet)
router.register(r"musical-genders", api.MusicalGenderViewSet)
router.register(r"occupations", api.OccupationViewSet)
router.register(r"movie-genders", api.MovieGenderViewSet)
router.register(r"social-medias", api.SocialMediaViewSet)
router.register(r"sports", api.SportViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Six Stripes API",
        default_version="v1",
        description=(
            "The data belonging to this database were collected and structured by the Sixstripes team "
            "through research and curators on the web, in free databases (Wikipedia) and digital platforms "
            "(Youtube and Sportify).<br>All profiles present are self-declared people belonging to the LGBTQ "
            "community.<br>All data collected has reference links as a way of verifying its veracity."
        ),
        contact=openapi.Contact(email=""),
    ),
    public=True,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("v1/", include(router.urls)),
    path("", schema_view.with_ui("redoc", cache_timeout=0), name="api-schema"),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
