from django.contrib import admin
from .models import Author , Book
# Register your models here.
admin.site.site_header = "Custom Admin Panel"
admin.site.site_title = 'BookStore Admin Panel'

class inlineBook(admin.TabularInline):
    model = Book
    extra = 1
# class inlineAuthor(admin.TabularInline):
#     model = Author
#     extra = 1
class BookAdmin(admin.ModelAdmin):
    fields = ('title','author','rating')
    list_display = ('title','author','rating')
    list_display_links = ('title','author')
    list_editable = ['rating']
    list_filter = ['author']
    search_fields = ['title']
    #inlines = [inlineAuthor]
class AuthorAdmin(admin.ModelAdmin):
    fields = ('name','birth_date','rating')
    list_display = ('name','birth_date','rating')
    list_editable = ['rating']
    list_filter = ('birth_date','rating')
    search_fields = ['name']
    inlines = [inlineBook]

admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)


