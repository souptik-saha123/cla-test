from django.http import HttpResponse

def index(request):
    value = request.GET.get("value")
    response = HttpResponse("")
    response["Set-Cookie"] = value  # Noncompliant
    response.set_cookie("sessionid", value)  # Noncompliant
    return response
  from django.http import HttpResponse

def index(request):
    value = request.GET.get("value")
    response = HttpResponse("")
    response["X-Data"] = value
    response.set_cookie("data", value)
    return response
