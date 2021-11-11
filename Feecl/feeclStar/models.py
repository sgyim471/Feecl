from django.db import models
from django.urls import reverse

# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField('Title', max_length=50)
    subject_teacher = models.CharField('Teacher', max_length=50)
    subject_star = models.FloatField('Star',default=0, null=True)

    def __str__(self):
        return "과목 : " + self.subject_name

    def get_absolute_url(self):
        return reverse("detail", args=[str(self.id)])