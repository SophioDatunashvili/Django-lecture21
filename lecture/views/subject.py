from django.urls import reverse, reverse_lazy

from lecture.models import Lecturer, Subject
from django.shortcuts import render, redirect
from lecture.forms import SubjectForm
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)


class Create(CreateView):
    model = Subject
    fields = "__all__"

    def get_success_url(self):
        return reverse("subject-detail", args=[self.object.pk])

    template_name = "subject/create.html"


class List(ListView):
    model = Subject

    context_object_name = "subjects"
    template_name = "subject/list.html"


class Detail(DetailView):
    model = Subject
    context_object_name = "subject"
    template_name = "subject/detail.html"


class Update(UpdateView):
    model = Subject
    fields = "__all__"

    def get_success_url(self):
        return reverse("subject-detail", args=[self.object.pk])

    template_name = "subject/update.html"


class Delete(DeleteView):
    model = Subject

    success_url = reverse_lazy("subject-list")

    def get(self, request, *args, **kwargs):
        return redirect("subject-list")

