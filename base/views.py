from django.shortcuts import render
from base.models import Person


# Create your views here.

def index(request):
    if request.method == "POST":
        name123 = request.POST.get("name")
        email123 = request.POST.get("email")
        message_all = request.POST.get("message")
        person = Person.objects.create(name=name123, email=email123, message=message_all)
        person.save()
    return render(request, "index.html")