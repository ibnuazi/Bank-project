from django.contrib import admin
from .models import *


admin.site.register(bankmodel)
admin.site.register(add_amount)
admin.site.register(withdraw_amount)

# Register your models here.
