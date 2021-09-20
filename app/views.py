from django.http.response import HttpResponse
from django.http.request import HttpRequest

def sum_double(request: HttpRequest, a, b) -> HttpResponse:
  if a == b:
    return HttpResponse((a+b) * 2)
  else:
    return HttpResponse(a+b)

def alarm_clock(request: HttpRequest, vacation, day) -> HttpResponse:
    if "True" in vacation:
        if day >= 1 and day <= 5:
            return HttpResponse('10:00')
        else:
            return HttpResponse('off')
    else:
        if day >= 1 and day <= 5:
            return HttpResponse('7:00')
        else:
            return HttpResponse('10:00')


def lucky_sum(request: HttpRequest, a, b, c) -> HttpResponse:
    if a == 13:
        return HttpResponse(0)
    elif b == 13:
        return HttpResponse(a)
    elif c == 13:
        return HttpResponse(a + b)
    else:
        return HttpResponse(a + b + c)
