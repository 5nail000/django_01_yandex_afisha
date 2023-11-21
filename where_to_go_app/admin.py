from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from .models import Place, PlaceImage


class PlaceImageInline(SortableInlineAdminMixin, admin.StackedInline):
    model = PlaceImage
    extra = 0
    readonly_fields = ('render_image_preview',)
    ordering_field = 'image_order'

    def render_image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="150" />', obj.image.url)
        else:
            return '(No image)'

    render_image_preview.short_description = 'Эскиз Изображения'


@admin.register(PlaceImage)
class PlaceImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    readonly_fields = ('render_image_preview',)
    list_display = ('__str__', 'render_image_preview', 'place')
    list_filter = ('place',)
    raw_id_fields = ('place',)

    def render_image_preview(self, image):
        return format_html('<img src="{}" style="max-height:200px" />', image.image.url)

    render_image_preview.short_description = 'Эскиз Изображения'


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('map_title', 'is_active')
    list_editable = ['is_active']
    search_fields = ['description_title']

    inlines = [PlaceImageInline]
