from django.contrib import admin
from .models import User, Person


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')
    exclude = ('creation_date', 'modification_date')


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    exclude = ('creation_date', 'modification_date')


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Person, PersonAdmin)
