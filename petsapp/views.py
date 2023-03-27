from django.shortcuts import render
from .models import Vaccines, Pet
# Create your views here.
def home(request):
    pets = Pet.objects.all()
    return render(request, 'home.html', {'pets': pets})