from django.contrib import admin
from rango.models import Category, Page

class CategoryAdmin(admin.ModelAdmin):
	prepolulated_fields = {'slug':('name',)}

# Register your models here.
admin.site.register(Category)
admin.site.register(Page)

