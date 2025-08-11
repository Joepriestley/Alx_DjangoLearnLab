from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    # Show these fields in the admin form
    fieldsets=UserAdmin.fieldsets+(
        ('Additional Information',{'fields':('date_of_birth','profile_photo')}),
    )
    list_display=('username','email','date_of_birth', 'is_staff')
admin.site.register(CustomUser, CustomUserAdmin)


class BookADmin(admin.ModelAdmin):
    list_display =('title','author','publication_year')
    list_filter=('title',)
    search_fields=('author','title')
admin.site.register(Book, BookADmin)
