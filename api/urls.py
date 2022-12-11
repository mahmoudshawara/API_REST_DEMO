from django.urls import path
from rest_framework import routers
from .views import AuthorViewSet , BookViewSet , FB_book ,FB_book_pk
from django.conf.urls import include

router = routers.DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('books', BookViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('FB_books/', FB_book),
    path('FB_books/<int:pk>', FB_book_pk),
]
