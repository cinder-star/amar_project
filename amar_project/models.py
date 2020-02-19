from django.db import models

# Create your models here.
class Sentences(models.Model):
    class Meta:
        db_table = "sentences"
    sentence = models.TextField(unique=True, null=False, blank=False)
    samples = models.IntegerField(default=0)
    verified = models.IntegerField(default=0)

class Recordings(models.Model):
    class Meta:
        db_table = "recordings"
    sentence = models.ForeignKey(Sentences, to_field="id", on_delete=models.CASCADE)
    filename = models.TextField(null=False, blank=False)