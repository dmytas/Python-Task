from django.db import models


class EmployeeManager(models.Manager):
    pass


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    objects = EmployeeManager()

    def __str__(self):
        return self.name
