from django.shortcuts import render
from django.http import HttpResponse

from .models import User


def index(request):
    context = {}
    user18 = User.objects.filter(bloodGroup=request.POST["bloodGroup"])
    print(f'\n{user18}\n')
    context['users'] = user18

    return render(request, 'home.html', context)


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['gender']
        email = request.POST['email']

        user = User(name=name, age=age, gender=gender, email=email)
        user.save()

        return HttpResponse("User registered successfully")

    return render(request, 'register.html')
