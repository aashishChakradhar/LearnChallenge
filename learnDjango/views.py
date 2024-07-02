from django.shortcuts import render
from django.views import View

# Create your views here.
# class login:
#     def login(request):
#         retrun HttpResponse(request,"login.html")
class Normal(View):
    def get(self, request):
        return render(request,"index.html")
