from django.contrib import admin
from application.models import *
from .models import enquiry_table

# Register your models here.

admin.site.register(enquiry_table)
admin.site.register(DropdownOption)
admin.site.register(company_work_details)

