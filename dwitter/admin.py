from re import U
from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Profile, Dweet
# Register your models here.

#making the user model from ER diagram 

class UserAdmin(admin.ModelAdmin):
    model = User 
    # Only display the "username" field
    fields = ["username"]


class ProfileInline(admin.StackedInline):
    model = Profile
    

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInline]
    


admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.unregister(Group)
admin.site.register(Dweet)
""" 
we don't want this decause will use something else
we create the new useradmin class cause we want extra features
like a user follow another user 
"""
# admin.site.register(Profile)