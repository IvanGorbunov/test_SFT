from django.contrib.admin import ModelAdmin


class BaseModelAdmin(ModelAdmin):
    list_display = (
        'id',
        'name',
        'created_at',
    )
    list_per_page = 25
    list_display_links = (
        'id',
        'name',
    )
    readonly_fields = ('created_at',)
    ordering = (
        'name',
    )

