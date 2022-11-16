from django.contrib import admin

from admin_site import models
from admin_site.models import Category
from admin_site.models import Vendor

admin.site.register(Category)

class Vendortadmin(admin.ModelAdmin):
    #list_display=('vendor_name')
    prepopulated_fields={'slug':('vendor_name',)}

admin.site.register(Vendor,Vendortadmin)
