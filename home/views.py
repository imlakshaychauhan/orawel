from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact

# Create your views here
def index(request):
     context={
           'variable':"this is variable from views.py"
     }
     return render(request, 'index.html', context)
      #return HttpResponse("Home")

def about(request):
      return render(request, 'about.html' )
     # return HttpResponse("about")

def contact(request):
      if request.method=="POST":
          name = request.POST.get('name')
          email = request.POST.get('email')
          desc = request.POST.get('desc')
          phone = request.POST.get('phone')
          contact=Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
          contact.save()
      return render(request, 'contact.html' )
      # return HttpResponse("services")

def services(request):
      return render(request, 'services.html' )
     # return HttpResponse("about")

      
