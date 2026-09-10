from django.contrib import admin
from .models import Breed, Kitten, KittenPhoto

class PhotoInline(admin.TabularInline):
    model = KittenPhoto
    extra = 1

@admin.register(Kitten)
class KittenAdmin(admin.ModelAdmin):
    list_display = ("name", "breed", "gender", "status", "price", "is_featured")
    list_filter = ("status", "gender", "breed")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    inlines = [PhotoInline]

admin.site.register(Breed)
