
from django.shortcuts import render, redirect,HttpResponse
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy

# Create your views here.
# class login:
#     def login(request):
#         retrun HttpResponse(request,"login.html")
class Normal(View):
    def get(self, request):
        return render(request,"index.html")

class Test(View):
    def get(self,request):
        message = request.session.get('message',False)
        if(message):del(request.session['message'])
        return render(request,"login.html",{'message':message})
    
    def post(self,request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username = username, password = password)
        if user is not None:# checks if the user is logged in or not?
            login(request,user) #logins the user
            return redirect('/home')
        else:
            request.session['message'] = "Invalid login"
            return redirect(request.path)

class AuthView(View):
    template_name = 'auth.html'

    def get(self, request):
        signup_form = UserCreationForm()#these are builtin forms from css
        login_form = UserCreationForm()
        return render(request, self.template_name, {'signup_form': signup_form, 'login_form': login_form})

    def post(self, request):
        if 'signup' in request.POST:
            signup_form = UserCreationForm(request.POST)
            login_form = AuthenticationForm()
            if signup_form.is_valid():
                signup_form.save()
                return redirect('login')
        elif 'login' in request.POST:
            signup_form = UserCreationForm()
            login_form = AuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                return redirect('home')  # redirect to your desired page
        else:
            signup_form = UserCreationForm()
            login_form = AuthenticationForm()

        return render(request, self.template_name, {'signup_form': signup_form, 'login_form': login_form})