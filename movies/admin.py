from django.contrib import admin
from .models import Person, Movie, Role

# Register your models here.


class RoleInLine(admin.TabularInline):
    model = Role
    extra = 1


class PersonAdmin(admin.ModelAdmin):
    inlines = (RoleInLine,)


class MovieAdmin(admin.ModelAdmin):
    inlines = (RoleInLine, )


admin.site.register(Person, PersonAdmin)
admin.site.register(Movie, MovieAdmin)