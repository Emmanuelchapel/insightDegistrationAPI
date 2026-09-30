from django.db import models

# Create your models here.

class Registration(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
      
    def __str__(self):
        return self.full_name