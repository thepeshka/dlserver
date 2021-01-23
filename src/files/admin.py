from django.contrib.admin import register, ModelAdmin, TabularInline
from .models import File, Version, Alias


class VersionInline(TabularInline):
    model = Version
    fields = (
        'name',
        'content',
        'hashid'
    )
    readonly_fields = 'hashid',


@register(Alias)
class AliasModel(ModelAdmin):
    pass


@register(File)
class FileModel(ModelAdmin):
    inlines = VersionInline,
