from django.contrib import admin

from .models import Form


class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","email")
    list_filter = ("occupation","date")
    search_fields = ("first_name","last_name","email")
    ordering = ("-first_name",)
    readonly_fields = ("occupation",)

admin.site.register(Form,FormAdmin)

