from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS_CHOICES = (
    ('BOUGHT', 'Bought'),
    ('PENDING', 'Pending'),
    ('NOT AVAILABLE', 'Not Available'),
)

class Item(models.Model):
    name = models.CharField(max_length=127)
    quantity = models.CharField(max_length=63)
    status = models.CharField( max_length=15, choices=STATUS_CHOICES, default='PENDING')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        return 'Item: ' + self.name