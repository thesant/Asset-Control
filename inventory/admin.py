from django.contrib import admin

# Register your models here.
from inventory.models import Category, Items, Priority


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ("id", "created", "modified", "categoryId",
                    "name", "brand", "model", "patrimony", "obs")


@admin.register(Priority)
class Priority(admin.ModelAdmin):
    list_display = ("id", "created", "modified",
                    "description", "classification")
