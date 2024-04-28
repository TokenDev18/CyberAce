from typing import Any
import math, datetime
from django.shortcuts import render
from django.db.models import Avg, Max, Min
from django.db import connection, OperationalError
from django.urls import reverse
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect
from .forms import CustomerForm, ChoiceForm, EmployeeForm, EngagementForm, PayrollForm, RequestForm, ServiceForm, VulnForm, UpdateForm, DeleteForm
from .models import Customers, Employees, Requests, Services, Vulnerabilities, Engagements, Payroll

# Create your views here.
def home(request):
    return render(request, 'home.html')

def reportView(request):
    context = {}
    sla_list = []

    context['customer_count'] = Customers.objects.count()
    context['engagement_count'] = Engagements.objects.count()
    
    #service data for reporting
    context['service_count'] = Services.objects.count()

    service_days = Services.objects.values_list('service_sla', flat=True)
    for days in service_days:
            days = int(days.replace(' days', '')) #replacing ' days' and converting to int
            sla_list.append(days)
    context['max_sla'] = str(max(sla_list)) + ' days'
    context['min_sla'] = str(min(sla_list)) + ' days'
    context['avg_sla'] = str(math.trunc(sum(sla_list) / len(sla_list))) + ' days'

    #employee data for reporting
    context['employee_count'] = Employees.objects.count()
    employee_salary = Payroll.objects.aggregate(Avg("salary"), Max("salary"), Min("salary"))
    context['employee_salary'] = math.trunc(employee_salary['salary__avg'])
    context['max_employee_salary'] = math.trunc(employee_salary['salary__max'])
    context['min_employee_salary'] = math.trunc(employee_salary['salary__min'])

    return render(request, 'reports.html', context)

def selectView(request):
    context = {}
    
    db_table = request.GET.get('table_name')
    form = ChoiceForm({})
    context['choice_form'] = ChoiceForm(request.GET)

    if request.method == 'GET':
        if db_table is None:
            return render(request, 'select_data.html', context)
        elif db_table == '1':
            context['customers'] = Customers.objects.all()
        elif db_table == '2':
            context['employees'] = Employees.objects.all()
        elif db_table == '3':
           context['engagements'] = Engagements.objects.all()
        elif db_table == '4':
            context['payroll'] = Payroll.objects.all()
        elif db_table == '5':
            context['requests'] = Requests.objects.all()
        elif db_table == '6':
            context['services'] = Services.objects.all()
        else: 
            context['vulnerabilities'] = Vulnerabilities.objects.all()
        return render(request, 'select_data.html', context)
    
    return render(request, 'select_data.html')

def deleteView(request):
    context = {}

    db_table = request.POST.get('table_name')
    row_id = request.POST.get('row_id')

    context['delete_form'] = DeleteForm(request.GET)

    if request.method == 'POST':
        if db_table is None:
            return render(request, 'delete_data.html', context)
        elif db_table == '1':
            delete_data(db_table, row_id) #calling delete data stored procedure
            return HttpResponseRedirect(reverse('delete_data'))
        elif db_table == '2':
            delete_data(db_table, row_id)
            return HttpResponseRedirect(reverse('delete_data'))
        elif db_table == '3':
            delete_data(db_table, row_id)
            return HttpResponseRedirect(reverse('delete_data'))
        elif db_table == '4':
            delete_data(db_table, row_id)
            return HttpResponseRedirect(reverse('delete_data'))
        elif db_table == '5':
            delete_data(db_table, row_id)
            return HttpResponseRedirect(reverse('delete_data'))
        elif db_table == '6':
            delete_data(db_table, row_id)
            return HttpResponseRedirect(reverse('delete_data'))
        else: 
            delete_data(db_table, row_id)
            return HttpResponseRedirect(reverse('delete_data'))
    return render(request, 'delete_data.html', context)

def updateView(request):
    context = {}

    db_table = request.GET.get('table_name')
    row_id = request.GET.get('row_id')

    context['update_form'] = UpdateForm(request.GET)

    if request.method == 'GET':
        if db_table is None: 
            return render(request, 'update_data.html', context)
        if db_table == '1':
            customer = Customers.objects.get(customer_id=row_id)
            form = CustomerForm({
                'customer_name': customer.customer_name, 
                'phone_number': customer.phone_number, 
                'company_address': customer.company_address, 
                'industry': customer.industry
            })
            context['table_form'] = form
        elif db_table == '2':
            employee = Employees.objects.get(employee_id=row_id)
            form = EmployeeForm({
                'first_name': employee.first_name,
                'last_name': employee.last_name,
                'job_title': employee.job_title, 
                'specialization': employee.specialization, 
                'date_hired': employee.date_hired
            })
            context['table_form'] = form
        elif db_table == '3':
            engagement = Engagements.objects.get(engagement_id=row_id)
            form = EngagementForm({
                'eng_customer': engagement.eng_customer,
                'service_id': engagement.service_id, 
                'begin_date': engagement.begin_date, 
                'end_date': engagement.end_date
            })
            context['table_form'] = form
        elif db_table == '4':
            payroll = Payroll.objects.get(payroll_id=row_id)
            form = PayrollForm({
                'pay_employee': payroll.pay_employee, 
                'salary': payroll.salary
            })
            context['table_form'] = form
        elif db_table == '5':
            customer_request = Requests.objects.get(request_id=row_id)
            form = RequestForm({
                'req_customer': customer_request.req_customer,
                'customer_req': customer_request.customer_req,
                'date_requested': customer_request.date_requested
            })
            context['table_form'] = form
        elif db_table == '6':
            service = Services.objects.get(service_id=row_id)
            form = ServiceForm({
                'serv_name': service.serv_name, 
                'serivce_sla': service.service_sla,
                'date_added': service.date_added
            })
            context['table_form'] = form
        else:
            vulns = Vulnerabilities.objects.get(vuln_id=row_id)
            form = VulnForm({
                'vuln_description': vulns.vuln_description, 
                'date_found': vulns.date_found,
                'severity': vulns.severity
            })
            context['table_form'] = form
    else:
        if db_table == '1':
            customer = Customers.objects.get(customer_id=row_id)
            customer.customer_name = request.POST.get('customer_name')
            customer.phone_number = request.POST.get('phone_number')
            customer.company_address = request.POST.get('company_address')
            customer.industry = request.POST.get('industry')
            customer.save()
            return HttpResponseRedirect(reverse('update_data'))
        elif db_table == '2':
            employee = Employees.objects.get(employee_id=row_id)
            employee.first_name = request.POST.get('first_name')
            employee.last_name = request.POST.get('last_name')
            employee.job_title = request.POST.get('job_title')
            employee.specialization = request.POST.get('specialization')
            employee.date_hired = request.POST.get('date_hired')
            employee.save()
            return HttpResponseRedirect(reverse('update_data'))
        elif db_table == '3':
            engagement = Engagements.objects.get(engagement_id=row_id)
            engagement.eng_customer = Customers.objects.filter(customer_id=row_id)[0]
            engagement.service_id = request.POST.get('service_id')
            engagement.begin_date = request.POST.get('begin_date')
            engagement.end_date = request.POST.get('end_date')
            engagement.save()
            return HttpResponseRedirect(reverse('update_data'))
        elif db_table == '4':
            payroll = Payroll.objects.get(payroll_id=row_id)
            converted_row_id = int(row_id) #convert row_id to int
            eID = converted_row_id + 200 #adding 200; employee ids start 200
            eID = str(eID) #converting back to string for db filtering
            payroll.pay_employee = Employees.objects.filter(employee_id=eID)[0]
            payroll.salary = request.POST.get('salary')
            payroll.save()
            return HttpResponseRedirect(reverse('update_data'))
        elif db_table == '5':
            customer_request = Requests.objects.get(request_id=row_id)
            customer_request.req_customer = Customers.objects.filter(customer_id=row_id)[0]
            customer_request.customer_req = request.POST.get('customer_req')
            customer_request.date_requested = request.POST.get('date_requested')
            customer_request.save()
            return HttpResponseRedirect(reverse('update_data'))
        elif db_table == '6':
            service = Services.objects.get(service_id=row_id)
            service.serv_name = request.POST.get('serv_name')
            service.service_sla = request.POST.get('service_sla')
            service.date_added = request.POST.get('date_added')
            service.save()
            return HttpResponseRedirect(reverse('update_data'))
        else:  
            vulns = Vulnerabilities.objects.get(vuln_id=row_id)
            vulns.vuln_description = request.POST.get('vuln_description')
            vulns.date_found = request.POST.get('date_found')
            vulns.severity = request.POST.get('severity')
            vulns.save()
            return HttpResponseRedirect(reverse('update_data'))
    return render(request, 'update_data.html', context)

def insertView(request):
    context = {}
    
    db_table = request.GET.get('table_name')
    form = ChoiceForm({})
    context['choice_form'] = ChoiceForm(request.GET)

    if request.method == 'GET':
        if db_table is None:
            return render(request, 'insert_data.html', context)
        elif db_table == '1':
            form = CustomerForm(request.GET)
        elif db_table == '2':
            form = EmployeeForm(request.GET)
        elif db_table == '3':
            form = EngagementForm(request.GET)
        elif db_table == '4':
            form = PayrollForm(request.GET)
        elif db_table == '5':
            form = RequestForm(request.GET)
        elif db_table == '6':
            form = ServiceForm(request.GET)
        else: 
            form = VulnForm(request.GET)
        context['table_form'] = form

        return render(request, 'insert_data.html', context)
    
    else: 
        if db_table == '1':
            customer = CustomerForm(request.POST)
            if customer.is_valid():
                customer_name = request.POST.get('customer_name')
                phone_number = request.POST.get('phone_number')
                company_address = request.POST.get('company_address')
                industry = request.POST.get('industry')
                customer_entry = Customers(customer_name=customer_name, phone_number=phone_number, company_address=company_address, industry=industry)

                try: 
                    customer_entry.save()
                except OperationalError as e:
                    context = {"message": e.args[1]}
                    return render(request, "duplicate_error.html", context)
    
                return HttpResponseRedirect(reverse('insert_data'))
        elif db_table == '2':
            employee = EmployeeForm(request.POST)
            if employee.is_valid():
                first_name = request.POST.get('first_name')
                last_name = request.POST.get('last_name')
                job_title = request.POST.get('job_title')
                specialization = request.POST.get('specialization')
                date_hired = request.POST.get('date_hired')
                employee_entry = Employees(first_name=first_name, last_name=last_name, job_title=job_title, specialization=specialization, date_hired=date_hired)
                
                try: 
                    employee_entry.save()
                except OperationalError as e:
                    context = {"message": e.args[1]}
                    return render(request, "duplicate_error.html", context)
                
                create_payroll_entry()
                return HttpResponseRedirect(reverse('insert_data'))
        elif db_table == '3':
            engagement = EngagementForm(request.POST)
            if engagement.is_valid():
                id = request.POST.get('eng_customer')
                customer = Customers.objects.filter(customer_id=id)[0]
                service_id = request.POST.get('service_id')
                begin_date = request.POST.get('begin_date')
                end_date = request.POST.get('end_date')
                engagement_entry = Engagements(eng_customer=customer, service_id=service_id, begin_date=begin_date, end_date=end_date)

                try: 
                   engagement_entry.save()
                except OperationalError as e:
                    context = {"message": e.args[1]}
                    return render(request, "duplicate_error.html", context)
                
                return HttpResponseRedirect(reverse('insert_data'))
        elif db_table == '4':
            payroll = PayrollForm(request.POST)
            if payroll.is_valid():
                id = request.POST.get('pay_employee')
                pay_employee = Employees.objects.filter(employee_id=id)[0]
                salary = request.POST.get('salary')
                payroll_entry = Payroll(pay_employee=pay_employee, salary=salary)

                try: 
                    payroll_entry.save()
                except OperationalError as e:
                    context = {"message": e.args[1]}
                    return render(request, "duplicate_error.html", context)

                return HttpResponseRedirect(reverse('insert_data'))
        elif db_table == '5':
            req = RequestForm(request.POST)
            if req.is_valid():
                id = request.POST.get('req_customer')
                req_customer = Customers.objects.filter(customer_id=id)[0]
                customer_req = request.POST.get('customer_req')
                requested = request.POST.get('date_requested')
                request_entry = Requests(req_customer=req_customer, customer_req=customer_req, date_requested=requested)
                request_entry.save() 
                return HttpResponseRedirect(reverse('insert_data'))
        elif db_table == '6':
            service = ServiceForm(request.POST)
            if service.is_valid():
                service_name = request.POST.get('serv_name')
                service_sla = request.POST.get('service_sla')
                date_added = request.POST.get('date_added')
                service_entry = Services(serv_name=service_name, service_sla=service_sla, date_added=date_added)

                try: 
                    service_entry.save()
                except OperationalError as e:
                    context = {"message": e.args[1]}
                    return render(request, "duplicate_error.html", context)
                
                return HttpResponseRedirect(reverse('insert_data'))
        else:
            vuln = VulnForm(request.POST)
            if vuln.is_valid():
                vuln_descript = request.POST.get('vuln_description')
                date_fnd = request.POST.get('date_found')
                sev = request.POST.get('severity')
                vuln_entry = Vulnerabilities(vuln_description=vuln_descript, date_found=date_fnd, severity=sev)
                vuln_entry.save()
                return HttpResponseRedirect(reverse('insert_data'))

def create_payroll_entry():
    employees = []
    employee_ids = Employees.objects.values_list('employee_id', flat=True)

    for id in employee_ids: #looping through employee queryset
        employees.append(id)
    
    new_employee = employees[-1] #last item in the list

    with connection.cursor() as cursor:
        cursor.callproc("create_payroll_entry", ['payroll', new_employee])
    pass

def delete_data(db_table, row_id):

    if db_table == '1':
        db_name = 'customers'
    elif db_table == '2':
        db_name = 'employees'
    elif db_table == '3':
        db_name = 'engagements'
    elif db_table == '4':
        db_name = 'payroll'
    elif db_table == '5':
        db_name = 'requests'
    elif db_table == '6':
        db_name = 'services'
    else:
        db_name = 'vulnerabilities'

    row_id = int(row_id)

    with connection.cursor() as cursor:
        cursor.callproc("delete_data", [db_name, row_id])
        results = cursor.fetchall()
    return results