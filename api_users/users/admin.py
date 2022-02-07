from django.contrib import admin

from .models import City, User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'first_name', 'last_name', 'other_name', 'email',
        'phone', 'birthday', 'city', 'additional_info', 'is_admin'
    )


class CityAdmin(admin.ModelAdmin):
    list_display = ('pk', 'city')


admin.site.register(User, UserAdmin)
admin.site.register(City)