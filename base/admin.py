from django.contrib import admin
from base.models import Item,Category,Tag

# Register your models here.

admin.site.register(Tag)
admin.site.register(Category)

admin.site.register(Item)

