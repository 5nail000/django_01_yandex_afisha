from django.contrib import admin
from .models import Place, PlaceImage
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.utils.html import format_html


class PlaceImageInline(SortableInlineAdminMixin, admin.StackedInline):
    model = PlaceImage
    extra = 0
    readonly_fields = ("image_preview",)
    ordering_field = "image_order"

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="150" />', obj.image.url)
        else:
            return "(No image)"

    image_preview.short_description = 'Image Preview'


class PlaceImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    readonly_fields = ("image_preview",)
    list_display = ('__str__', 'image_preview', 'place')
    list_filter = ('place',)

    def image_preview(self, obj):
        return format_html('<img src="{}" height="150" />', obj.image.url)

    image_preview.short_description = 'Image Preview'


# Register your models here.
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('map_title', 'is_active')
    list_editable = ['is_active']
    inlines = [PlaceImageInline]


admin.site.register(Place, PlaceAdmin)
admin.site.register(PlaceImage, PlaceImageAdmin)
