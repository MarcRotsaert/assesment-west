from django.shortcuts import render

# Create your views here.
def lowest(request):
    if request.method=="GET":
        # print(request.body)
        print(dir(request))
        num = request.GET.get("number", None)
        print(num)
        print(request.content_params)
        print("lowest")
        return render(request, "base.html")

