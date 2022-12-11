from django.urls import path
from rest_framework import routers
from .views import AuthorViewSet , BookViewSet
from django.conf.urls import include

router = routers.DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('books', BookViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
