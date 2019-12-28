from django.contrib import admin

from . models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('name','blood_group','status')
    search_fields = ['blood_group']


admin.site.register(User,UserAdmin)
