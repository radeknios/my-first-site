from django.contrib import admin
from .models import Profile, Post, Available, Category


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']

admin.site.register(Profile, ProfileAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'body', 'publish', 'location')

admin.site.register(Post, PostAdmin)

class AvailableAdmin(admin.ModelAdmin):
    list_display = ('user', 'start', 'end')

class CategoryAdmin(admin.ModelAdmin):
    list_dispaly = ('name', 'parent', 'slug')

admin.site.register(Available, AvailableAdmin)
admin.site.register(Category)






