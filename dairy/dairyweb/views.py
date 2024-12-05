from django.contrib import messages
from django.shortcuts import render
from .models import Contact

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def Aboutus(request):
    return render(request,'About us.html')

def Noh(request):
    return render(request, 'Noh.html')

def fof(request):
    return render(request,'fof.html')

def PB(request):
    return render(request,'PB.html')

def AN(request):
    return render(request,'AN.html')

def contact(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        phone = request.POST['phone']
        discription = request.POST['discription']

        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(discription) < 4:
            messages.error(request, "Please fill the form correctly")
        else:
            tanmay = Contact(email=email, name=name, phone=phone,  discription=discription)
            tanmay.save()
            messages.success(request, "Your enquiry has been successfully sent")
    return render(request,'contact.html')



def products(request):
    return render(request,'products.html')

def milk(request):
    return render(request,'milk.html')

def mdahi(request):
    return render(request,'malai dahi.html')