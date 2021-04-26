from djongo import models
from django import forms

# Create your models here.
class Option(models.Model):
    id = models.CharField(max_length=5) # question id + option id
    text = models.TextField()
    class Meta:
        abstract = True
    def __str__(self):
        self.text()

class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = [
            'id','text',
        ]

class Question(models.Model):
    id = models.CharField(max_length=3)
    question_text = models.TextField()
    right = models.CharField(max_length=5) #right option id
    options = models.ArrayField(
        model_container=Option,
        model_form_class=OptionForm
    )
    class Meta:
        abstract = True
    
    def __str__(self):
        return self.question_text
    
    
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'id', 'question_text', 'right', 'options'
        ]

class Category(models.Model):
    _id = models.ObjectIdField()
    id = models.CharField(max_length=3)
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
    def __str__(self):
        return self.name
    def check_list(self):
        list = []
        for i in self.questions:
            list.append(i.right)
        return list