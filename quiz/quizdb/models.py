from djongo import models
from django import forms

# Create your models here.
class Option(models.Model):
    id = models.CharField(max_length=2)
    text = models.TextField()
    class Meta:
        abstract = True

class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = [
            'id','text',
        ]

class Question(models.Model):
    id = models.CharField(max_length=3)
    question_text = models.TextField()
    right = models.CharField(max_length=1)
    options = models.ArrayField(
        model_container=Option,
        model_form_class=OptionForm
    )
    class Meta:
        abstract = True
    
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'id', 'question_text', 'right', 'options'
        ]

class Category(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=20)
    questions = models.ArrayField(
        model_container=Question,
        model_form_class= QuestionForm,
        null = False,
        blank = False
    )
    objects = models.DjongoManager()
    def get_img_path(self):
        return '/img/'+ self.img