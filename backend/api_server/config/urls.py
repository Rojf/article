from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from articles import views

# router = routers.SimpleRouter()
# router.register(r'articles', views.ArticlesView, basename='articles')

urlpatterns = [
    path("", include("articles.urls")),
    path("api/v1/articles/", include("articles.urls")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
