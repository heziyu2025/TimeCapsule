from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Capsule

class CapsuleInline(admin.TabularInline):  
    model = Capsule
    extra = 1 

class CustomUserAdmin(UserAdmin):
    inlines = (CapsuleInline,)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
