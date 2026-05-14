from django.db import models

# Create your models here.
class TimeStampModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateField(auto_now=True)
    
    class Meta:
        abstract=True 