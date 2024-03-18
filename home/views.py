from django.shortcuts import render, HttpResponse,redirect
from django.http import JsonResponse
from datetime import datetime
import random
from home.models import *

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

def quiz(request):
    context = {'categories':Category.objects.all()}
    if request.GET.get('category'):
        return redirect(f"/quiz/?category={request.GET.get('category')}")
    return render(request,'quiz.html',context)

def takequiz(request):
    
    return render(request, 'takequiz.html')
    
#for createing an api
def get_quiz(request):
    try:
        question_objs=Question.objects.all()
        if request.GET.get('category'):
            question_objs=question_objs.filter(category__category_name__icontains=request.GET.get('category'))
        question_objs=list(question_objs)    
        data=[]
        random.shuffle(question_objs)
        
        for question_obj in question_objs:
            data.append({
                "Category":question_obj.category.category_name,
                "Question":question_obj.question,
                "Marks":question_obj.marks,
                "Answer":question_obj.get_answers(),
            })
            
        payload = {'status':True,'data': data}
        return JsonResponse(payload)
    except Exception as e:
        print(e)
    return HttpResponse('Error Occured')