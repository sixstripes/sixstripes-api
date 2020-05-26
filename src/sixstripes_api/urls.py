from data import api
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from invitations import api as invitations_api
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
router.register(r"sexual-orientations", api.SexualOrientationViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Six Stripes API",
        default_version="v1",
        description=(
            """
            Making way for representation through data, the Sixstripes API enables researchers, journalists,
            students, businesses and more to explore, understand, and connect to a more diverse and
            representative world.
            <br>
            All data made available through this API was collected and structured by the Sixstripes team
            and/or by volunteers through research and curation of open databases and digital platforms.
            <br>
            Every person represented in a profile is self-declared as part of the LGBTQ community and all
            collected data has reference links as a way of verifying its veracity.
            """
        ),
        contact=openapi.Contact(email=""),
    ),
    permission_classes=[],
    public=True,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("v1/", include(router.urls)),
    path("v1/countries/", api.CountryView.as_view(), name="list-countries"),
    path("invites/", invitations_api.InviteCreateAPIView.as_view(), name="create-invite"),
    path("suggestions/", invitations_api.DataSuggestionAPIView.as_view(), name="create-suggestion"),
    path("", schema_view.with_ui("redoc", cache_timeout=0), name="api-schema"),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
