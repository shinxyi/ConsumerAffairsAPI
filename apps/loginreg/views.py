# from django.shortcuts import render
# from django.core.urlresolvers import reverse
from .models import User
from .forms import RegisterForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register(request):
    if request.method == "POST":
        print '***'
        print request.POST
        print request.POST['first_name']
        response = HttpResponse()
        user = User.userManager.register(
            request.POST.get('username', False),
            request.POST.get('first_name', False),
            request.POST.get('last_name', False),
            request.POST.get('email', False),
            request.POST.get('password', False),
            request.POST.get('confirm_password', False)
            )
        if 'error' in user:
            return HttpResponse('Passwords do not match.')
        bound_form = RegisterForm(request.POST)
        if bound_form.is_valid():
            user = user['user']
            # user = User.userManager.create(username=user['username'],first_name= user['first_name'], last_name= user['last_name'], email= user['email'], password= user['password'])
            user = User.userManager.create(user)
            user.save()
            print user.id
            response['user'] = user
        else:
            print bound_form.errors
            for key in bound_form.errors:
                response[key] = bound_form.errors[key]
        return response
    else:
        return HttpResponse('Please submit a POST request...')
