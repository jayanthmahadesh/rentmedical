from django.contrib import admin
from manipal1.models import category
from manipal1.models import subproducts
from manipal1.models import ord
# Register your models here.
admin.site.register(category),
admin.site.register(subproducts),
admin.site.register(ord)
# admin.site.register(subproducts),
# admin.site.register(product)
