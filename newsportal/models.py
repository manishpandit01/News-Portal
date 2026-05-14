from django.db import models

# Create your models here.
class TimeStampModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateField(auto_now=True)
    
    class Meta:
        abstract=True 
        
class Category(TimeStampModel):
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering=["name"]
        verbose_name="category"
        verbose_name_plural="Categories"
        
class Tag(TimeStampModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    