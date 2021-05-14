from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class Consumer(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Transgender', 'Transgender'),
        ('Not to Specify', 'Not to Specify'),
    )
    BLOOD_TYPE = (
        ('A+', 'A+'),
        ('B+', 'B+'),
        ('AB+', 'AB+'),
        ('O+', 'O+'),
        ('A-', 'A-'),
        ('B-', 'B-'),
        ('AB-', 'AB-'),
        ('O-', 'O-'),
        ('NA', 'NA')
    )
    MARITAL_STATUS_TYPE = (
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Widowed', 'Widowed'),
        ('Divorced', 'Divorced'),
    )

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=14, choices=GENDER)
    date_of_birth = models.DateField()
    marital_status = models.CharField(max_length=8, choices=MARITAL_STATUS_TYPE)
    blood_group = models.CharField(max_length=3, choices=BLOOD_TYPE)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=200)
    phone = models.PositiveBigIntegerField()
    email = models.EmailField()

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
