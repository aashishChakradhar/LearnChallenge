from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
# Create your views here.
def index(request):
    # context = {
    #     'variable1': 'this is variable1 sent',
    #     'variable2': 'this is variable2 sent'
    # }
    return render(request,'index.html')
    # return HttpResponse('This is homepage.')
def about(request):
    return render(request,'about.html')
    # return HttpResponse('This is about page.')
def contact(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        contact = Contact(fname = fname, lname = lname, email = email, phone=phone, comment = comment, date = datetime.today())
        contact.save()
    return render(request,'contact.html')
    # return HttpResponse('This is contact page.')
def services(request):
    return render(request,'services.html')
    # return HttpResponse('This is services page.')