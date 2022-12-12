from django.urls import path
from rest_framework import routers
from .views import AuthorViewSet,BookViewSet ,FB_book ,FB_book_pk ,FB_author,FB_author_pk,CB_book,CB_book_pk,CB_author,CB_author_pk
from django.conf.urls import include

router = routers.DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('books', BookViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('FB_books/', FB_book),
    path('FB_books/<int:pk>', FB_book_pk),
    path('FB_authors/', FB_author),
    path('FB_authors/<int:pk>', FB_author_pk),
    path('CB_books/', CB_book.as_view()),
    path('CB_books/<int:pk>', CB_book_pk.as_view()),
    path('CB_authors/', CB_author.as_view()),
    path('CB_authors/<int:pk>', CB_author_pk.as_view()),
]
