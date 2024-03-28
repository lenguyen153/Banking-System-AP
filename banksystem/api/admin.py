from django.contrib import admin

from .models import (
    Bank,
    Branch,
    Account,
)

admin.site.register(Branch)
admin.site.register(Bank)
