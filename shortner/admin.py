from shortner.models import links
from django.contrib import admin
class linksAdmin(admin.ModelAdmin):
    pass
admin.site.register(links,linksAdmin)
