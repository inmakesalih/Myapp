from django.contrib import admin

# Register your models here.
from . models import category,product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock','available','updated','created']
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(product,ProductAdmin)