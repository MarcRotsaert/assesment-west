from django.shortcuts import render

# Create your views here.
def lowest(request):
    if request.method=="GET":
        print("lowest")
        return render(request, "base.html")
