from django.shortcuts import render
from .serializers import AuthorSerializer , BookSerializer
from .models import Author , Book
from rest_framework import viewsets , status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import  AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
# GET POST DELETE PUT wit ViewSets.
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','rating','birth_date']
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title','author__name']
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
# GET PUT DELETE
@api_view(['GET','PUT','DELETE'])
def FB_book_pk(request,pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist: 
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

@api_view(['GET','POST'])
def FB_author(request):
    if request.method == 'GET':
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors , many=True)
        return Response (serializer.data)
    elif request.method == 'POST':
        serializer = AuthorSerializer (data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data , status = status.HTTP_201_CREATED)
        return Response (serializer.data ,status = status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def FB_author_pk(request,pk):
    try:
        author = Author.objects.get(pk=pk)
    except author.DoesNotExist:
        return Response (status = sta.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = AuthorSerializer (author , many = False)
        return Response (serializer.data)
    elif request.method == 'PUT':
        serializer = AuthorSerializer (author , request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        author.delete()
        return Response (status =status.HTTP_204_NO_CONTENT)
# class Based Views
class CB_book(APIView):
    def get(self,request):
        books = Book.objects.all()
        serializer = BookSerializer (books , many=True)
        return Response (serializer.data)
    def post(self,request):
        serializer = BookSerializer (data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data , status=status.HTTP_201_CREATED)
        return Response (serializer.errors , status =status.HTTP_400_BAD_REQUEST)
class CB_book_pk(APIView):
    def get_book(self,pk):
        try :
            book = Book.objects.get(pk=pk)
            return book
        except book.DoesNotExist:
            return Response (status = status.HTTP_404_NOT_FOUND)
    def get (self, request, pk):
        book = self.get_book(pk)
        serializer = BookSerializer (book , many=False)
        return Response (serializer.data)
    def put (self,request,pk):
        book = self.get_book (pk)
        serializer = BookSerializer (book,request.data)
        if serializer.is_valid():
            serializer.save()
            return (serializer.data)
        return Response (serializer.errors , status =status.HTTP_400_BAD_REQUEST)
    def delete (self,request,pk):
        book = self.get_book(pk)
        book.delete()
        return Response (status = status.HTTP_204_NO_CONTENT)
class CB_author(APIView):
    def get(self,request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors , many=True)
        return Response (serializer.data )
    def post (self, request):
        serializer = AuthorSerializer (data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status =status.HTTP_201_CREATED)
        return Response (status=status.HTTP_400_BAD_REQUEST)
class CB_author_pk(APIView):
    def get_author(self,pk):
        try:  
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            return Response (status = status.HTTP_404_NOT_FOUND)
    def get (self , request , pk):
        author = self.get_author(pk)
        serializer = AuthorSerializer (author , many = False)
        return Response (serializer.data)
    def put (self , request , pk):
        author = self.get_author(pk)
        serializer = AuthorSerializer (author , request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    def delete (self , request , pk):
        author = self. get_author (pk)
        author.delete()
        return Response (status = status.HTTP_204_NO_CONTENT)
        




