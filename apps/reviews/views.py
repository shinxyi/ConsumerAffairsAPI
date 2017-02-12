from ..companies.models import Company
from ..loginreg.models import User
from .models import Review
from .forms import ReviewCreationForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from ipware.ip import get_ip

@csrf_exempt
def create(request, company_id, uuid):
    if request.method == "POST":
        response = HttpResponse()
        user = User.userManager.filter(auth_token=uuid)
        if len(user)<1:
            response.write('Invalid authenticity token.')
            return response
        else:
            user= user[0]
        company = Company.objects.filter(id=company_id)
        if len(company)<1:
            response.write('No such company to review.')
            return response
        else:
            company= company[0]

        bound_form = ReviewCreationForm(request.POST)
        if bound_form.is_valid():
            review = Review.objects.create(
                title=request.POST['title'],
                rating=request.POST['rating'],
                summary=request.POST['summary'],
                ip_address= get_ip(request),
                user=user,
                company=company
                )
            review.save()
            response.write('Thank you. Your review for {} has been submitted.'.format(company.name))
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
    reviews = Review.objects.filter(user=user)
    for review in reviews:
        response.write('Date/Time: {} \n'.format(str(review.created_at)))
        response.write('Title: {} \n'.format(str(review.title)))
        response.write('Rating: {}\n'.format(str(review.rating)))
        response.write('Summary: {}\n'.format(str(review.summary)))
        response.write('Company: {}\n'.format(str(review.company.name)))
        response.write('User: {} {}\n'.format(str(review.user.first_name), str(review.user.last_name)))
        response.write('User Ip Address: {}\n'.format(str(review.ip_address)))
        response.write('Submitted at: {}\n\n'.format(str(review.created_at)))
    return response
