from .models import Company
from ..loginreg.models import User
from .forms import CompanyCreationForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create(request, uuid):
    if request.method == "POST":
        response = HttpResponse()
        user = User.userManager.filter(auth_token=uuid)
        if len(user)<1:
            response.write('Invalid authenticity token.')
            return response
        else:
            user= user[0]
        bound_form = CompanyCreationForm(request.POST)
        if bound_form.is_valid():
            company = Company.objects.create(
                name=bound_form.cleaned_data['name'],
                location=bound_form.cleaned_data['location'],
                industry=bound_form.cleaned_data['industry'],
                current_status=bound_form.cleaned_data['current_status'],
                website=bound_form.cleaned_data['website'],
                service_description=bound_form.cleaned_data['service_description'],
                created_by = user
                )
            company.save()
            response.write('Thank you. {} is now part of the database.'.format(company.name))
        else:
            print bound_form.errors
            for key in bound_form.errors:
                response.write(str(key) + str(bound_form.errors[key]))
        return response
    else:
        return HttpResponse('Please submit a POST request...')

@csrf_exempt
def index(request, uuid):
    response = HttpResponse()
    user = User.userManager.filter(auth_token=uuid)
    if len(user)<1:
        response.write('Invalid authenticity token.')
        return response
    companies = Company.objects.all()
    for company in companies:
        response.write('Name: {} \n'.format(str(company.name)))
        response.write('Location: {}\n'.format(str(company.location)))
        response.write('Industry: {}\n'.format(str(company.industry)))
        response.write('Current Status: {}\n'.format(str(company.current_status)))
        response.write('Website: {}\n'.format(str(company.website)))
        response.write('Description: {}\n\n'.format(str(company.service_description)))
    return response

@csrf_exempt
def get_one(request, company_name, uuid):
    response = HttpResponse()
    user = User.userManager.filter(auth_token=uuid)
    if len(user)<1:
        response.write('Invalid authenticity token.')
        return response
    company= Company.objects.filter(name=company_name)
    if len(company)<1:
        response.write('No company with such name.')
    else:
        company = company[0]
        response.write('Id: {} \n'.format(str(company.id)))
        response.write('Name: {} \n'.format(str(company.name)))
        response.write('Location: {}\n'.format(str(company.location)))
        response.write('Industry: {}\n'.format(str(company.industry)))
        response.write('Current Status: {}\n'.format(str(company.current_status)))
        response.write('Website: {}\n'.format(str(company.website)))
        response.write('Description: {}\n'.format(str(company.service_description)))
    return response
