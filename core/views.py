from django.shortcuts import render


def home(request):
    return render(request,'home.html')


def aboutme(request):
    title = "About Me"
    paragraph = "Something short and leading about the collection below—its contents, the creator, etc. Make it short and sweet."
    return render(request,'aboutme.html',{"title":title,"paragraph":paragraph})
    
def contactme(request):
    title="contact me"
    paragraph="hello"
    return render(request,'contactme.html',{"title":title,"paragraph":paragraph})
    
def readme(request):
    title="contact me"
    paragraph="hello arun"
    return render(request,'readme.html',{"title":title,"paragraph":paragraph})
