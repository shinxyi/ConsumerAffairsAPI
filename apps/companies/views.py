from .models import Company
from .forms import CompanyCreationForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create(request):
    if request.method == "POST":
        response = HttpResponse()
        bound_form = CompanyCreationForm(request.POST)
        if bound_form.is_valid():
            company = Company.objects.create(
                name=request.POST['name'],
                location=request.POST['location'],
                industry=request.POST['industry'],
                current_status=request.POST['current_status'],
                website=request.POST['website'],
                service_description=request.POST['service_description']
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
def index(request):
    pass

@csrf_exempt
def get_one(request, id):
    pass
