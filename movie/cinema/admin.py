from django.contrib import admin

from .models import Category, Image
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('name',)
   
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    '''Admin View for Image'''

    list_display = ('title','category','image')
    list_filter = ('category',)