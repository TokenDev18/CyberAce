# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Customers(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    company_address = models.CharField(max_length=255)
    industry = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.customer_name

    class Meta:
        managed = False
        db_table = 'customers'
    


class Employees(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    specialization = models.CharField(max_length=50)
    date_hired = models.DateTimeField(blank=True, null=True)
    date_terminated = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        employee_name = self.first_name + ' ' + self.last_name
        return employee_name

    class Meta:
        managed = False
        db_table = 'employees'


class Engagements(models.Model):
    engagement_id = models.AutoField(primary_key=True)
    eng_customer = models.ForeignKey(Customers, on_delete=models.CASCADE, db_column='eng_customer')
    service_id = models.IntegerField()
    begin_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'engagements'


class Payroll(models.Model):
    payroll_id = models.AutoField(primary_key=True)
    pay_employee = models.ForeignKey(Employees, on_delete=models.CASCADE, db_column='pay_employee')
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'payroll'


class Requests(models.Model):
    request_id = models.AutoField(primary_key=True)
    req_customer = models.ForeignKey(Customers, on_delete=models.CASCADE, db_column='req_customer')
    customer_req = models.TextField()
    date_requested = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requests'


class Services(models.Model):
    service_id = models.AutoField(primary_key=True)
    serv_name = models.CharField(max_length=30)
    service_sla = models.CharField(max_length=10)
    date_added = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'services'


class Vulnerabilities(models.Model):
    vuln_id = models.AutoField(primary_key=True)
    vuln_description = models.TextField()
    date_found = models.DateTimeField(blank=True, null=True)
    severity = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'vulnerabilities'
