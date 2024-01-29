import time
from django.shortcuts import render

# Create your views here.
def lowest(request):
    if request.method=="GET":
        # print(request.body)
        print(dir(request))
        num = request.GET.get("number", None)
        
        if num is not None:
            result = return_lowest(int(num))
            print("lowest")
            print(result)
            return render(request, "base.html", context={"lowest": result})
        else:
            return render(request, "base.html")

def return_lowest(val_in: int):
    number_lowest = val_in
    test = True
    while test:
        test = False
        for ind in range(val_in-1, 1, -1):
            reminder = number_lowest % ind
            if reminder:
                test = True
                if ind == val_in-1:
                    number_lowest += (val_in-2)*val_in
                    break
                else:
                    number_lowest += (val_in-1)*val_in

    return number_lowest


print(return_lowest(25))
print(time.process_time())
print(return_lowest(7))
print(return_lowest(6))
print(return_lowest(5))