from django.shortcuts import render,redirect
from django.http import HttpResponse

# def home(request):
#     return HttpResponse ("hello arun")

def about_page(request):
    obj = {
        "customer_details": {"id": "1", "name": "Arun"},
        "customer_users": [
            {"user_id": 1, "user_name": "Rohit"},
            {"user_id": 2, "user_name": "Piyush"},
            {"user_id": 3, "user_name": "Sparsh"},
            {"user_id": 4, "user_name": "Ram"},
        ]
    }
    return render(request,"tables.html",context={"obj":obj})



