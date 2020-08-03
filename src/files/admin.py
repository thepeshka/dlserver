from django.contrib.admin import register, ModelAdmin, TabularInline
from .models import File, Version


class VersionInline(TabularInline):
    model = Version
    fields = (
        'name',
        'content',
        'hashid'
    )
    readonly_fields = 'hashid',


@register(File)
class FileModel(ModelAdmin):
    inlines = VersionInline,
