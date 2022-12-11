from django.shortcuts import render
from .serializers import AuthorSerializer , BookSerializer
from .models import Author , Book
from rest_framework import viewsets , status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# GET POST DELETE PUT wit ViewSets.
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
# Function Based Views
#GET POST
@api_view(['GET','POST'])
def FB_book(request):
    #GET
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response (serializer.data)
    #POST
    elif request.method == 'POST':
        serializer = BookSerializer (data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def FB_book_pk(request,pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExists: 
        return Response (status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = BookSerializer(book, many=False)
        return Response (serializer.data)
    elif request.method == 'PUT':
        serializer = BookSerializer (book, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors , status =status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        book.delete()
        return Response (status= status.HTTP_204_NO_CONTENT)





