from django.urls import path, include
from rest_framework.routers import DefaultRouter


from . import views


router = DefaultRouter()
router.register(r"authors", views.AuthorViewSet, basename="author")
router.register(r"books", views.BookViewSet, basename="book")


urlpatterns = [
    path("", views.index, name="index"),
    path("", include(router.urls))
]
