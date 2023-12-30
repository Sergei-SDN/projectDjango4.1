from django.contrib import admin

from Category.models import Category


# Register your models here.

# admin.site.register(Category)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
