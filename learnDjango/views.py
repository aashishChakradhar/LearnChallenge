from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
def index(response):
    response = """<html>
    <head></head>
    <body>
    <h1>hello</h1>
    </body>
    </html>"""
    return HttpResponse(response)
