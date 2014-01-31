from django.contrib import admin

from .models import Presentation
from slides.asset.models import Asset

# Register your models here.

class AssetInline(admin.TabularInline):
    model = Presentation.assets.through

class PresentationAdmin(admin.ModelAdmin):
    inlines = [
        AssetInline,
    ]

admin.site.register(Presentation, PresentationAdmin)
