from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class OtdResource(resources.ModelResource):
    class Meta:
        model = Otd

class OtdAdmin(ImportExportModelAdmin):
    resource_class = OtdResource
# Register your models here.
admin.site.register(Otd, OtdAdmin)