from django import forms
from .models import Subject, Lecturer


class LecturerForm(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = "__all__"


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = "__all__"
