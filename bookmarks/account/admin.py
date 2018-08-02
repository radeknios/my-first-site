from django.contrib import admin
from .models import Profile, Post, Available, Category, SubCategory


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']

admin.site.register(Profile, ProfileAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'body', 'publish', 'location')

admin.site.register(Post, PostAdmin)

class AvailableAdmin(admin.ModelAdmin):
    list_display = ('user', 'start', 'end')

admin.site.register(Available, AvailableAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_dispaly = ('category', 'slug')

admin.site.register(Category, CategoryAdmin)

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('subcategory', 'category', 'slug')

admin.site.register(SubCategory, SubCategoryAdmin)







