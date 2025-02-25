from django.contrib import admin

# Register your models here.
from .models import Author, Book, Publisher

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')

class BookAdmin(admin.ModelAdmin):
   list_display = ('title', 'publisher', 'publication_date')
   list_filter = ('publication_date','publisher')
   date_hierarchy = 'publication_date'
   ordering = ('title',)
   fields = ('title', 'authors', 'publisher', 'publication_date')
   filter_horizontal = ('authors',)
   raw_id_fields = ('publisher',)



#admin.site.register(Author)
#admin.site.register(Book)
admin.site.register(Publisher)

admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)