from django import forms
from .models import Customers, Employees, Engagements, Payroll, Requests, Services, Vulnerabilities

class ChoiceForm(forms.Form):

    DBTABLES = (
        (1, 'Customers'), 
        (2, 'Employees'), 
        (3, 'Engagements'), 
        (4, 'Payroll'),
        (5, 'Requests'), 
        (6, 'Services'), 
        (7, 'Vulnerabilities')
    )
    table_name = forms.ChoiceField(choices=DBTABLES)

class UpdateForm(forms.Form):
    DBTABLES = (
        (1, 'Customers'), 
        (2, 'Employees'), 
        (3, 'Engagements'), 
        (4, 'Payroll'),
        (5, 'Requests'), 
        (6, 'Services'), 
        (7, 'Vulnerabilities')
    )

    table_name = forms.ChoiceField(choices=DBTABLES)
    row_id = forms.CharField()

class DeleteForm(forms.Form):
    DBTABLES = (
        (1, 'Customers'), 
        (2, 'Employees'), 
        (3, 'Engagements'), 
        (4, 'Payroll'),
        (5, 'Requests'), 
        (6, 'Services'), 
        (7, 'Vulnerabilities')
    )

    table_name = forms.ChoiceField(choices=DBTABLES)
    row_id = forms.CharField()

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ('customer_name', 'phone_number', 'company_address', 'industry')
        #labels = {'customer': 'input customer name'}

class EmployeeForm(forms.ModelForm):
    class Meta: 
        model = Employees
        fields = ('employee_id', 'first_name', 'last_name', 'job_title', 'specialization', 'date_hired')

class EngagementForm(forms.ModelForm):
    class Meta:
        model = Engagements
        fields = ('eng_customer', 'service_id', 'begin_date', 'end_date')

class PayrollForm(forms.ModelForm):
    class Meta: 
        model = Payroll
        fields = ('pay_employee', 'salary')

class RequestForm(forms.ModelForm):
    class Meta: 
        model = Requests
        fields = ('req_customer', 'customer_req', 'date_requested')

class ServiceForm(forms.ModelForm):
    class Meta: 
        model = Services
        fields = ('serv_name', 'service_sla', 'date_added')

class VulnForm(forms.ModelForm):
    class Meta: 
        model = Vulnerabilities
        fields = ('vuln_description', 'date_found', 'severity')
