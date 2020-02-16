from django.shortcuts import render

# Create your views here.


def recorder(request):
    return render(request=request, template_name="index.html", context=None)
