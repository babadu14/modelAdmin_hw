from django.contrib import admin
from shop.models import Category, Item, Tag, Image

from django.contrib.contenttypes.admin import GenericStackedInline
# Register your models here.

class CategoryInline(GenericStackedInline):
    model = Image
    extra = 1

class ItemInline(GenericStackedInline):
    model = Image
    extra = 1

class CategoryItemInline(admin.TabularInline):
    model = Item
    extra = 1

class CategotyAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']
    ordering = ['name']
    inlines = [CategoryItemInline, CategoryInline]


class ItemTagInline(admin.StackedInline):
    model = Tag.items.through
    extra = 1

class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'description']
    search_fields = ['name', 'description']
    ordering = ['-price']
    inlines = [ItemTagInline, ItemInline]
    

class TagAdmin(admin.ModelAdmin):
    list_display =['name']
    search_fields = ['name']

admin.site.register(Category, CategotyAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Tag, TagAdmin)