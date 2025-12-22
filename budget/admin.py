from django.contrib import admin
from budget.models import Category, Transaction, EcoScore

admin.site.register(Transaction)
admin.site.register(Category)
admin.site.register(EcoScore)
