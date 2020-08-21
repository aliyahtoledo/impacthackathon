from django.db import models


class Demand(models.Model):
    cropName = models.CharField(max_length=1000)
    orderDate = models.DateField()
    orderType = models.CharField(max_length=1000)
    arrivalDate = models.DateField()
    partnerName = models.CharField(max_length=1000)
    quantity = models.IntegerField(default=0)
    unitPrice = models.DecimalField(max_digits=12, decimal_places=2)
    amount = models.DecimalField(max_digits=12, decimal_places=2)


class Sales(models.Model):
    demand = models.ForeignKey(Demand, default=1, on_delete=models.CASCADE)
    cropName = models.CharField(max_length=1000)
    salesDate = models.DateField()
    quantity = models.IntegerField(default=0)

    def monthofSales(self):
        return self.salesDate.strftime('%B')