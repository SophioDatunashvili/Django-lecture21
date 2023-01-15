from django.urls import path
from .views import lecturer, subject

urlpatterns = [
    path("lecturer/create", lecturer.Create.as_view(), name="lecturer-create"),
    path("lecturer/", lecturer.List.as_view(), name="lecturer-list"),
    path("lecturer/<int:pk>/", lecturer.Detail.as_view(), name="lecturer-detail"),
    path("lecturer/<int:pk>/update", lecturer.Update.as_view(), name="lecturer-update"),
    path("lecturer/<int:pk>/delete", lecturer.Delete.as_view(), name="lecturer-delete"),

    path("subject/create", subject.Create.as_view(), name="subject-create"),
    path("subject/", subject.List.as_view(), name="subject-list"),
    path("subject/<int:pk>/", subject.Detail.as_view(), name="subject-detail"),
    path("subject/<int:pk>/update", subject.Update.as_view(), name="subject-update"),
    path("subject/<int:pk>/delete", subject.Delete.as_view(), name="subject-delete"),
]
