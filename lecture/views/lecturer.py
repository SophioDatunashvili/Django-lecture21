from django.urls import reverse, reverse_lazy

from lecture.models import Lecturer
from django.shortcuts import render, redirect
from lecture.forms import LecturerForm
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)


class Create(CreateView):
    model = Lecturer
    fields = "__all__"

    def get_success_url(self):
        return reverse("lecturer-detail", args=[self.object.pk])

    template_name = "lecturer/create.html"


class List(ListView):
    model = Lecturer

    context_object_name = "lecturers"
    template_name = "lecturer/list.html"


class Detail(DetailView):
    model = Lecturer
    context_object_name = "lecturer"
    template_name = "lecturer/detail.html"


class Update(UpdateView):
    model = Lecturer
    fields = "__all__"

    def get_success_url(self):
        return reverse("lecturer-detail", args=[self.object.pk])

    template_name = "lecturer/update.html"


class Delete(DeleteView):
    model = Lecturer

    success_url = reverse_lazy("lecturer-list")

    def get(self, request, *args, **kwargs):
        return redirect("lecturer-list")
