from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator 
# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField('Title', max_length=50)
    subject_teacher = models.CharField('Teacher', max_length=50)
    subject_star = models.FloatField('Star',default=0, null=True)

    def __str__(self):
        return "과목 : " + self.subject_name

    def get_absolute_url(self):
        return reverse("detail", args=[str(self.id)])

class Comment(models.Model):
    comment_text = models.CharField('Text', max_length=400)
    comment_star = models.PositiveBigIntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(5)])
    updated_at = models.DateTimeField(auto_now=True)
    subject_id = models.ForeignKey('Subject',on_delete=models.CASCADE)

    def __str__(self):
        return '별점 : ' + str(self.comment_star)