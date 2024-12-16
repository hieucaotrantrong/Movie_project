from django.urls import path, re_path, include
from django.contrib import admin
from moviegeeks import views

urlpatterns = [
    # The home page
    path("", views.index, name="index"),
    # Movie-related URLs
    path("movies/", include("moviegeeks.urls")),
    # Collector app URLs
    path("collect/", include("collector.urls")),
    # Analytics app URLs
    path("analytics/", include("analytics.urls")),
    # Admin panel
    path("admin/", admin.site.urls),
    # Recommender app URLs
    path("rec/", include("recommender.urls")),
]
