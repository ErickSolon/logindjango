from django.contrib import admin
from .models import loot, logip

# Register your models here.

class LootAdmin(admin.ModelAdmin):
    list_display_links = ("id", "email")
    list_editable = ("senha",)
    list_per_page = 10
    list_filter = ("email",)
    list_display = ("id", "email", "senha")
    search_fields = ("email",)

class IpAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ("ip",)

admin.site.register(loot, LootAdmin)
admin.site.register(logip, IpAdmin)
