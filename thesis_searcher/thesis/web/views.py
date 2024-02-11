from django.shortcuts import render

def index(request):
    my_dict = {"insert_me": "I am from views.py"}
    return render(request,'myfirst.html',context=my_dict)