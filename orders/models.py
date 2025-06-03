from django.db import models


class Order(models.Model):
    item_name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[('success', 'Success'), ('failed', 'Failed')])
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item_name} - {self.status}"
