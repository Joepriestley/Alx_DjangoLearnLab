from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.admin import UserAdmin
from django.contrib.contenttypes.models import ContentType
from .models import Book, CustomUser

# Custom User Admin
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    list_display = ('username', 'email', 'date_of_birth', 'is_staff')

admin.site.register(CustomUser, CustomUserAdmin)


# Book Admin
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('title',)
    search_fields = ('author', 'title')

admin.site.register(Book, BookAdmin)


# Automatically create groups and assign permissions
def setup_groups_and_permissions():
    # Get Book content type
    book_content_type = ContentType.objects.get_for_model(Book)

    # Define custom permissions
    view_book_permission, _ = Permission.objects.get_or_create(
        codename='can_view_books',
        name='Can View Books',
        content_type=book_content_type
    )

    add_book_permission = Permission.objects.get(codename='add_book')
    change_book_permission = Permission.objects.get(codename='change_book')
    delete_book_permission = Permission.objects.get(codename='delete_book')

    # Create or update "Librarian" group
    librarian_group, _ = Group.objects.get_or_create(name='Librarians')
    librarian_group.permissions.set([
        add_book_permission,
        change_book_permission,
        delete_book_permission,
        view_book_permission
    ])

    # Create or update "Reader" group
    reader_group, _ = Group.objects.get_or_create(name='Readers')
    reader_group.permissions.set([view_book_permission])


# Hook into Django's admin ready signal
from django.apps import apps
from django.db.models.signals import post_migrate

def create_groups_after_migrate(sender, **kwargs):
    if sender.name == 'your_app_name':  # Replace with your app name
        setup_groups_and_permissions()

post_migrate.connect(create_groups_after_migrate)
