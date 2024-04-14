from django.db import models
    
# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_no = models.IntegerField(default=0)
    password = models.CharField(max_length=100)  # For simplicity, should be hashed
    registration_date = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    ward = models.CharField(max_length=100)
    street = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.surname}"
