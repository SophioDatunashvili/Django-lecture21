from django.urls import path
from .views import lecturer

urlpatterns = [
    path("lecturer/create", lecturer.create, name="lecturer-create"),
    path("lecturer/", lecturer.list_all, name="lecturer-list"),
    path("lecturer/<int:pk>/", lecturer.detail, name="lecturer-detail"),
    path("lecturer/<int:pk>/update", lecturer.update, name="lecturer-update"),
    path("lecturer/<int:pk>/delete", lecturer.delete, name="lecturer-delete"),
]
