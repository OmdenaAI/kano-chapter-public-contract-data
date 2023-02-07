from django.db import models

# Create your models here.
# models.py
from django.db import models

class Project(models.Model):
    contract_title = models.CharField(max_length=255)
    budget_amount = models.DecimalField(max_digits=15, decimal_places=2)
    contract_amount = models.DecimalField(max_digits=15, decimal_places=2)
    contractor=models.CharField(max_length=255)
    lga = models.CharField(max_length=255)
    mda = models.CharField(max_length=255)
    # other fields here

    def formatted_amount(self):
        return "N{:,.2f}".format(self.budget_amount)

    def formatted_contract(self):
        return "N{:,.2f}".format(self.contract_amount)

    def __str__(self):
        return self.contractor
