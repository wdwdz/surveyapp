from django.forms import ModelForm
from .models import Todo
from django.forms import RadioSelect
from django import forms

class TodoForm(ModelForm):

    MODE_CHOICES =(('formal','Formal'),
                        ('Informal','Informal'))
    
    ACTIVITY_CHOICES =(('individual','Individual'),
                        ('collaborative','Collaborative'))

    LIKERT_CHOICES =(('Strongly disagree','Strongly disagree'),
                        ('Disagree','Disagree'),
                        ('Neither agree nor disagree','Neither agree nor disagree'),
                        ('Agree','Agree'),
                        ('Strongly agree','Strongly agree'))

    learningmode = forms.ChoiceField(choices=MODE_CHOICES, widget=forms.RadioSelect())
    learningactivity = forms.ChoiceField(choices=ACTIVITY_CHOICES, widget=forms.RadioSelect())
    ambient = forms.ChoiceField(choices=LIKERT_CHOICES, widget=forms.RadioSelect())
    spatial = forms.ChoiceField(choices=LIKERT_CHOICES, widget=forms.RadioSelect())    
    ergonomic = forms.ChoiceField(choices=LIKERT_CHOICES, widget=forms.RadioSelect())
    infrastructure = forms.ChoiceField(choices=LIKERT_CHOICES, widget=forms.RadioSelect())
    people = forms.ChoiceField(choices=LIKERT_CHOICES, widget=forms.RadioSelect())
    rules = forms.ChoiceField(choices=LIKERT_CHOICES, widget=forms.RadioSelect())
    individual = forms.ChoiceField(choices=LIKERT_CHOICES, widget=forms.RadioSelect())
    virtual = forms.ChoiceField(choices=LIKERT_CHOICES, widget=forms.RadioSelect())

    # title = forms.CharField(label='What is your title?')

    class Meta:
        model = Todo
        fields = ['learningmode', 'learningactivity', 'ambient','spatial','ergonomic','infrastructure','people','rules','individual','virtual']
    