from django.db import models


class Lecturer(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=150)
    picture = models.ImageField(upload_to="lecturer/", blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Subject(models.Model):
    name = models.CharField(max_length=150)
    start_date = models.DateField()
    duration = models.CharField(max_length=150)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE, related_name="subjects")

    def __str__(self):
        return self.name
