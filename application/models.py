from time import timezone
from django.db import models
from datetime import date
from django.contrib.auth.models import User


class company_work_details(models.Model):
    company_name = models.CharField(max_length=255)
    address = models.TextField()
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=10)
    requirement = models.CharField(max_length=100)
    payment = models.CharField(max_length=100)
    date_field = models.DateField(default=date.today)

    def __str__(self):
        return self.company_name


class DropdownOption(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class enquiry_table(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name