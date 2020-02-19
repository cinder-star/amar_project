import os

from django.shortcuts import render
from django.forms import Form
from django.http import HttpResponse, Http404
from django.core.files.storage import FileSystemStorage
from django.db import transaction

from amar_recorder.settings import BASE_DIR
from .models import Sentences, Recordings

# Create your views here.


def recorder(request):
    sentence = Sentences.objects.all().order_by("samples").first()
    return render(
        request=request,
        template_name="index.html",
        context={"filename": str(sentence.id), "text": sentence.sentence},
    )


@transaction.atomic
def record(request):
    if request.method == "POST":
        directory = os.path.join(BASE_DIR, "media")
        myform = Form(request.POST, request.FILES)
        file = myform.files["audio"]
        filename = request.POST.get("filename", None)
        sentence_no = filename.split("-")[0]
        fs = FileSystemStorage(location=directory)
        x = fs.save(filename, file)
        recording = Recordings(sentence_id=sentence_no, filename=filename)
        recording.save()
        sentence = Sentences.objects.get(id=sentence_no)
        sentence.samples = sentence.samples + 1
        sentence.save()
        return HttpResponse()
    return HttpResponse()
