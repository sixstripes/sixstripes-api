from data import api
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"politicians", api.PoliticianViewSet)
router.register(r"musicians", api.MusicianViewSet)
router.register(r"movies", api.MovieViewSet)
router.register(r"digital-influencers", api.DigitalInfluencerViewSet)
router.register(r"athlets", api.AthletViewSet)
router.register(r"scientists", api.ScientistViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Six Stripes API",
        default_version="v1",
        description="",
        terms_of_service="",
        contact=openapi.Contact(email=""),
        license=openapi.License(name="License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
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
