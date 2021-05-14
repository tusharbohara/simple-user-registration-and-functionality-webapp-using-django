from django import forms
from tempus_dominus.widgets import DatePicker


class ConsumerRegistrationForm(forms.Form):
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Transgender', 'Transgender'),
        ('Not to Specify', 'Not to Specify'),
    ]
    BLOOD_TYPE = [
        ('A+', 'A+'),
        ('B+', 'B+'),
        ('AB+', 'AB+'),
        ('O+', 'O+'),
        ('A-', 'A-'),
        ('B-', 'B-'),
        ('AB-', 'AB-'),
        ('O-', 'O-'),
    ]
    MARITAL_STATUS_TYPE = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Widowed', 'Widowed'),
        ('Divorced', 'Divorced'),
    ]

    first_name = forms.CharField(label='Enter First Name', required=True)
    last_name = forms.CharField(label='Enter Last Name', required=True)
    gender = forms.ChoiceField(choices=GENDER)
    date_of_birth = forms.DateField(
        widget=DatePicker(
            options={
                'ignoreReadonly': True,
            },
            attrs={
                'append': 'fa fa-calendar',
            }
        )
    )
    blood_group = forms.ChoiceField(choices=BLOOD_TYPE)
    marital_status = forms.ChoiceField(choices=MARITAL_STATUS_TYPE)
    country = forms.CharField(label='Country', required=True)
    state = forms.CharField(label='State', required=False)
    district = forms.CharField(label='District', required=False)
    city = forms.CharField(label='City', required=True)
    phone = forms.IntegerField(required=True)
    email = forms.EmailField(required=True)
