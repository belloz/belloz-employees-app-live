from django import forms
from .models import Employees


class AddEmployee(forms.ModelForm):
    class Meta:
        model = Employees
        fields = (
            'first_name',
            'last_name',
            'email',
            'address',
            'state',
            'postal_code',
            'city',
            'date_of_birth',
            'phone_number',
            'employed_from',

            'sin',
            'position',
            'wage',
            'driver_lic',
            'wsib',
            'status',
            'clothes_size',
            'whmis',
            'work_heights',
            'worker_health_safety',
            'propane_in_construction',
            'note',
        )
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'employed_from': forms.DateInput(attrs={'class': 'form-control'}),

            'sin': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.Select(attrs={'class': 'form-control'}),
            'wage': forms.TextInput(attrs={'class': 'form-control'}),
            'driver_lic': forms.TextInput(attrs={'class': 'form-control'}),
            'wsib': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'clothes_size': forms.Select(attrs={'class': 'form-control'}),
            'whmis': forms.Select(attrs={'class': 'form-control'}),
            'work_heights': forms.Select(attrs={'class': 'form-control'}),
            'worker_health_safety': forms.Select(attrs={'class': 'form-control'}),
            'propane_in_construction': forms.Select(attrs={'class': 'form-control'}),
            'note': forms.Textarea(attrs={'class': 'form-control'}),
        }


