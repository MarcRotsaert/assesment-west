# import asyncio
import multiprocessing
from typing import Union
import time
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.
def lowest(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        num = request.GET.get("number", None)

        if num is not None:
            try:
                with multiprocessing.Pool(processes=1) as pool:
                    result = pool.map(return_lowest, [int(num)])[0]
                # print(result)
                result = "result for " + num + ':\n ' + str(result)
                context = {"lowest": result}
            except ValueError:
                context = {"lowest": "fill in integer"}
            return render(request, "base.html", context=context)

        else:
            return render(request, "base.html")


def return_lowest(val_in: int, max_runtime: float = 30) -> Union[str, int]:
    start_time = time.time()

    number_lowest = val_in
    test = True
    while test:
        test = False
        if time.time()-start_time > max_runtime:
            number_lowest = "Takes too long"
            break

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
