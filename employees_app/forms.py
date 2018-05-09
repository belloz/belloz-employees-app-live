from django import forms
from .models import Employees


class AddEmployee(forms.ModelForm):
    class Meta:
        model = Employees
        fields = (
            'first_name',
            'last_name',
            'address',
            'state',
            'postal_code',
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
