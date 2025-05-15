from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    # enrollment_date = models.DateField(auto_now_add=True)
    # address = models.CharField(max_length=255)
    # phone_number = models.CharField(max_length=15, blank=True, null=True)
    # profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"