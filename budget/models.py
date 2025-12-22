from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)
    eco_friendly = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    item_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.item_name} – ${self.amount}"

class EcoScore(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    monthly_target = models.PositiveIntegerField(default=5)
    eco_transactions_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} – Eco: {self.eco_transactions_count}/{self.monthly_target}"
