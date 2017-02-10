# from django.shortcuts import render
# from django.core.urlresolvers import reverse
from .models import User
from .forms import RegisterForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register(request):
    if request.method == "POST":
        response = HttpResponse()
        bound_form = RegisterForm(request.POST)
        if bound_form.is_valid():
            user = User.userManager.register(
                request.POST['username'],
                request.POST['first_name'],
                request.POST['last_name'],
                request.POST['email'],
                request.POST['password'],
                request.POST['confirm_password']
                )
            if 'error' in user:
                return HttpResponse('Passwords do not match.')
            user = user['user']
            user = User.userManager.create(
                username=user['username'],
                first_name= user['first_name'],
                last_name= user['last_name'],
                email= user['email'],
                password= user['password'],
                auth_token= user['auth_token']
                )
            user.save()
            response.write(str(user.auth_token))
        else:
            print bound_form.errors
            for key in bound_form.errors:
                response.write(str(key) + str(bound_form.errors[key]))
        return response
    else:
        return HttpResponse('Please submit a POST request...')

@csrf_exempt
def login(request):
    if request.method == "POST":
        response = HttpResponse()
        user = User.userManager.login(request.POST['email'],request.POST['password'])
        if 'errors' in user:
            print user['errors']
            for error in user['errors']:
                response.write(error)
        else:
            response.write(user['user'])
        return response
    else:
        return HttpResponse('Please submit a POST request...')

@csrf_exempt
def test(request, uuid):
    response = HttpResponse()
    user = User.userManager.filter(auth_token=uuid)
    if len(user)<1:
        response.write('Invalid Authentication Token.')
    else:
        response.write(str(user[0].first_name))
    return response
