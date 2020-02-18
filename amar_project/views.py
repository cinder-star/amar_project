import os
from datetime import datetime

from django.shortcuts import render
from django.forms import Form
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

from amar_recorder.settings import BASE_DIR

# Create your views here.


def recorder(request):
    now = datetime.now()
    filename = now.strftime("%Y%m%d%H%M%s")
    return render(request=request, template_name="index.html", context={"filename": filename, "text": "আমি ভাত খাই"})

def record(request):
    if request.method == 'POST':
        directory = os.path.join(BASE_DIR, "media")
        myform = Form(request.POST, request.FILES)
        file = myform.files["audio"]
        filename = request.POST.get("filename", None)
        fs = FileSystemStorage(location=directory)
        x = fs.save(filename, file)
    return HttpResponse()